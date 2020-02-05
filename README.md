# trudo_project

**Рекомендованная версия**: Python 3.7

**Набор пакетов Python для установки в виртуальное окружение:** в файле requirements.txt

**Задание:** реализовать приложение (бэкенд и фронтенд) для поиска сотрудников компании в списке


Задание выполнено, ниже приведено описание выполненного задания для трех категорий лиц: конечного пользователя, разработчика-желающего доработать код, разработчика-желающего выложить реализацию на своем сервере.

**1. Конкретный пример реализации для конечного пользователя - сайт в интернете**

На сайте **http://138.201.80.90:8888/** выложен весь список сотрудников министерства. Для поиска конкретного сотрудника вбиваем его полные ФИО с пробелами после слэша. Например, **http://138.201.80.90:8888/Иванова Анастасия Николаевна** осуществит поиск по таблице сотрудников и выдаст нам сотрудника с ФИО=Иванова Анастасия Николаевна.
Некорректный ввод ФИО предупредит нас об ошибке.

**2. Разработчику, желающему выложить эту реализацию на своем сервере**

Команда **docker pull azamatgainullin/trudo3** делает локальную копию репозитория с https://hub.docker.com/ .
Команда **docker run -p 8888:8888 azamatgainullin/trudo3** осуществляет запуск кода из репозитория на локальном порту хоста 8888. Теперь реализация доступна в интернете по адресу: ваш IP:8888.


**3. Разработчику, желающему доработать код**

Запуск команды **git clone https://github.com/AzamatGainullin/trudo_project** осуществляет загрузку исходных файлов с https://github.com/.








 
 


