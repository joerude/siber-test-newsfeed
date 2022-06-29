## Table of Contents
- [Task](#задача-лента-новостей)
- [Preparing](#preparing)
- [Launch](#launch)
- [1. Docker](#1-docker-compose)
- [2. Local](#2-local)
- [Structure](#structure-tree)


# Тестовое задание для кандидата на вакансию Python Developer

## Задача: Лента новостей

Cоздать ленту новостей с формой добавления новости на базе web-приложения.
Каждая новость должна содержать:

* заголовок,
* дату публикации,
* тело новости (текстовый формат),
* картинки (опционально).

Отображение ленты новостей должно поддерживать постраничный вывод с регулируемым
количеством новостей на странице: 10, 20 и 50.
Отображаться должны все элементы новости. 

### Требования к технологиям
Django, Django Forms, БД: MySQL или PostgreSQL
Дополнительным плюсом будет использование технологий контейнеризации для деплоймента.

### Требования к формату представления результата
Выполненное ТЗ должно быть собрано в архив формата .gzip, .bzip2 или .zip и включать в себя:

— Инструкцию по сборке (если проект собирается частями), а также инструкцию по использованию
на английском языке.

— В случаях, где необходимо, дополнительные файлы со структурой БД, конфигурацией приложения
и т.д.

Решения, не удовлетворяющие требованиям, рассматриваться не будут.


## Preparing

The service consists of two components: Django Project and PostgreSQL database, so for its successful operation it is required
the following software:

- [Python 3](https://www.python.org/downloads/) >=3.6;
- [PostgreSQL](https://www.postgresql.org/docs/current/tutorial-start.html) >=13 launching database server 
- or [Docker](https://www.docker.com/get-started) >=20.10.14, if database server is not available.


## Launch

After installing the required software, you need to download (clone) the source code of
the service and go to the directory with the source code:

```shell
git clone https://github.com/joerude/sibers-test-newsfeed.git
cd sibers-test-newsfeed
```


### 1. [Docker Compose](https://docs.docker.com/compose/gettingstarted/)

Probably the most "painless" and simplest way. Both components of the system (django project and database) 
are deployed in separate Docker containers. The settings of the components are specified in
[docker-compose.yml](https://github.com/joerude/sibers-test-newsfeed/blob/master/docker-compose.yml).

```shell
docker-compose up
```

### 2. Local
Set `DEBUG=1` in [.env](https://github.com/joerude/sibers-test-newsfeed/blob/master/.env) file

Also configure your Postgres Database settings:
```shell
# LOCAL_DB_NAME=your_db
# LOCAL_DB_USER=your_username
# LOCAL_DB_PASSWORD=your_password
# LOCAL_DB_HOST=localhost
# LOCAL_DB_PORT=5432
```

```shell
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python3 manage.py runserver
```

Go to the link: http://0.0.0.0:8000/ or http://127.0.0.1:8000/

To be able to add news, you must be logged in

## Structure (Tree)

```
├── config                 
│      └── settings         # django projetc settings directory  
├── media                   # media files (images)
├── data                    # docker volumes
├── newsfeed                # main app folder
│   ├── migrations
├── staticfiles             # static css, js files 
│   ├── admin
│   ├── ckeditor
│   ├── css
│   └── debug_toolbar 
└── templates
    └── newsfeed
        └── block
```
