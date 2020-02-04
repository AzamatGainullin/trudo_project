### ИМПОРТ НЕОБХОДИМЫХ БИБЛИОТЕК ###
import requests
from bs4 import BeautifulSoup
import pandas as pd
import joblib
import os

### ФУНКЦИИ ДЛЯ ПАРСИНГА ПЕРЕЧНЯ СОТРУДНИКОВ ###
def get_html(url):
    r = requests.get(url)
    return r.text

def get_page_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    employees = soup.find('div',
                      class_='employees-list').find_all('div', class_="item")
    page_data = []
    for user in employees:
        try:
            name = user.find('div', class_='name' ).text.strip().replace('\xa0', ' ')
            position = user.find('div', class_='position' ).text.strip()
            info = user.find('div', class_='info' ).text.strip().replace('\n', ', ')
            data = {'ФИО':name, 'Должность':position, 'Контакты':info}
            page_data.append(data)
        except:
            pass
    return page_data

### ПАРСИНГ ПЕРЕЧНЯ СОТРУДНИКОВ (ЕСЛИ ПАРСИНГ НЕ ПРОВОДИЛСЯ РАНЕЕ) ###
### СОХРАНЕНИЕ ПЕРЕЧНЯ СОТРУДНИКОВ В ФОРМАТАХ CSV, PKL ###
try:
    spisok_sotrudnikov = joblib.load('spisok_sotrudnikov_as_pkl.pkl')
    print('Загружен ранее скачанный перечень сотрудников')
except:
    url = 'http://mincultrk.ru/o_ministerstve/spisok_sotrudnikov/'
    html = get_html(url)
    page_data = get_page_data(html)
    spisok_sotrudnikov = pd.DataFrame(page_data)
    spisok_sotrudnikov.to_csv('spisok_sotrudnikov_as_csv.csv')
    joblib.dump(spisok_sotrudnikov, 'spisok_sotrudnikov_as_pkl.pkl')
    print('С сайта минкультуры скачан перечень сотрудников')

### ИНИЦИАЛИЗАЦИЯ Flask ###
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

### БЛОК РАБОТЫ С БАЗОЙ ДАННЫХ (ВЫГРУЗКА, ЗАГРУЗКА, КОНВЕРТИРОВАНИЕ) ###
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///spisok_sotrudnikov_as_db.db'
db = SQLAlchemy(app)

class ITEMS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80), unique=False, nullable=False)
    Position = db.Column(db.String(80), unique=False, nullable=False)
    Kontakt = db.Column(db.String(80), unique=False, nullable=False)
    def __repr__(self):
        return "(%r, %r, %r)" % (self.Name, self.Position, self.Kontakt)
    def to_dict(self):
        return {'ФИО':self.Name, 'Должность':self.Position, 'Контакты':self.Kontakt}

try:
    item = ITEMS.query.all()
    print('Загружена ранее созданная база данных сотрудников')
except:
    db.create_all()
    objects = []
    for i in range(len(spisok_sotrudnikov)):
        item = ITEMS(Name=spisok_sotrudnikov.loc[i]['ФИО'],
                     Position=spisok_sotrudnikov.loc[i]['Должность'],
                     Kontakt=spisok_sotrudnikov.loc[i]['Контакты'])
        objects.append(item)
    db.session.bulk_save_objects(objects)
    db.session.commit()
    item = ITEMS.query.all()
    print('Создана база данных сотрудников')
    

frontend_example = pd.DataFrame([i.to_dict() for i in item])

### СОЗДАНИЕ МАРШРУТОВ ПРЕДСТАВЛЕНИЯ ДАННЫХ, ЗАПУСК FLASK-ПРИЛОЖЕНИЯ ###
@app.route('/')
def all():
    return frontend_example.to_html()

@app.route('/<username>')
def user(username):
    to_show = frontend_example[frontend_example.ФИО==username]
    if len(to_show)>0:
        return to_show.to_html()
    else:
        return 'ВВЕДИТЕ КОРРЕКТНЫЕ ФИО'
    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8888)))
