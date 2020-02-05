# trudo_project

**Рекомендованная версия**: Python 3.7

**Набор пакетов Python для установки в виртуальное окружение:** в файле requirements.txt

**Задание:** реализовать приложение (бэкенд и фронтенд) для поиска сотрудников компании в списке.


Задание выполнено, ниже приведено описание выполненного задания для трех категорий лиц: конечного пользователя, разработчика-желающего доработать код, разработчика-желающего выложить реализацию на своем сервере.

**1. Конкретный пример реализации для конечного пользователя - сайт в интернете**

На сайте **http://138.201.80.90:8888/** выложен весь список сотрудников министерства. Для поиска конкретного сотрудника вбиваем его полные ФИО с пробелами после слэша. Например,
**http://138.201.80.90:8888/Иванова Анастасия Николаевна** осуществит поиск по таблице сотрудников и выдаст нам сотрудника с ФИО=Иванова Анастасия Николаевна.
Некорректный ввод ФИО предупредит нас об ошибке.

**2. Разработчику, желающему выложить эту реализацию на своем сервере**

Команда **docker pull azamatgainullin/trudo3** делает локальную копию репозитория с https://hub.docker.com/ .
Команда **docker run -p 8888:8888 azamatgainullin/trudo3** осуществляет запуск кода из репозитория на локальном порту хоста 8888. Теперь реализация доступна в интернете по адресу: ваш IP:8888.


**3. Разработчику - описательная часть реализации**

Запуск команды **git clone https://github.com/AzamatGainullin/trudo_project** осуществляет загрузку исходных файлов с https://github.com/.

Подробнее о реализации поставленной задачи.

Задача была рассмотрена более широко.
Были реализованы следующие этапы (весь код ввиду простоты выложен в одном файле app.py, запуск которого и приводит к запуску веб-сервера с сайтом на локальном хосте):

- парсинг первоначального списка сотрудников с сайта url = 'http://mincultrk.ru/o_ministerstve/spisok_sotrudnikov/'. Использована библиотека BeautifulSoup4. Причем парсинг запускается единоразово, если программа не обнаружит ранее скачанный список сотрудников. Сделано для удобства и недопущения излишней нагрузки на оригинальный сайт со списком сотрудников;
- конвертация списка сотрудников в форматы pd.DataFrame, CSV, PKL с дальнешим сохранением на локальном диске. Формат pd.DataFrame из библиотеки анализа данных pandas предоставляет широчайшие возможности для фильтрации данных, дальнейшей конвертации данных в CSV или HTML форматы для рендеринга на странице сайта. Что и было использовано;
- инициализация приложения Flask (веб-сервер) в связке с форматом базы данных sqlite, создание базы данных с таблицей ITEMS, соответствующей списку сотрудников. Конвертация списка сотрудников в формат базы данных и сохранение на локальном диске. Причем процедуры создания базы данных и конвертации запускаются единоразово, в случае если не запускались ранее;
- обратная загрузка базы данных в программу, конвертация данных для подготовки к рендерингу (отображению на сайте);
- присвоение приложение Flask маршрутов отображения данных, в зависимости от того, что введено в адресной строке. Передача динамического URL как переменной в функцию, в которой происходит отбор в pd.DataFrame по данной переменной. Такая функция и позволяет нам осуществлять поиск по ФИО сотрудника.

Таким образом, продемонстрированы практические навыки использования следующих технологий:

- язык программирования Python
- парсинг данных в интернете с помощью BeautifulSoup4
- запуск веб-сервера на Flask
- использование баз данных
- динамический рендеринг веб-страницы по запросу пользователя
- технологии Git для публичного размещения кода на https://github.com/.
- технологии контейнеризации Docker с публичным размещением на https://hub.docker.com/.





 
 


