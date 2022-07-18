![example workflow](https://github.com/DenisShahbazyan/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)
# Yamdb

## Описание:
Сайт является - базой отзывов о фильмах, книгах и музыке. Пользователи могут оставлять рецензии на произведения, а также комментировать эти рецензии. Администрация добавляет новые произведения и категории (книга, фильм, музыка и т.д.)

## Развертывание:
### Запуск веб-сервера::
- Склонируйте проект на Ваш компьютер 
```sh 
git clone https://github.com/DenisShahbazyan/yamdb_final.git
``` 
- Перейдите в папку с проектом 
```sh 
cd yamdb_final
``` 
- Создайте и активируйте виртуальное окружение 
```sh 
python -m venv venv 
source venv/Scripts/activate 
``` 
- Обновите менеджер пакетов (pip) 
```sh 
pip install --upgrade pip 
``` 
- Установите необходимые зависимости 
```sh 
pip install -r ./api_yamdb/requirements.txt
``` 
- Создайте миграции
```sh
python ./api_yamdb/manage.py makemigrations
python ./api_yamdb/manage.py migrate
```
- Создайте суперпользователя
```sh
python ./api_yamdb/manage.py createsuperuser
```
- Запуск сервера
```sh
python ./api_yamdb/manage.py runserver
```
- Сайт запуститься по адресу http://127.0.0.1:8000
- Спецификация API будет доступна http://127.0.0.1:8000/redoc/

### Запуск docker-контейнера:
- В папке `infra` создайте файл `.env` - в нем будут храниться переменные окружения для проекта. Пример его содержимого ниже:
```sh
SECRET_KEY=SECRET_KEY
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```
- Запуск docker-compose
```sh
cd infra/
docker-compose up -d
```
- Выполните миграции
```sh
sudo docker-compose exec web python3 manage.py makemigrations 
sudo docker-compose exec web python3 manage.py migrate 
```
- Создайте суперпользователя
```sh
sudo docker-compose exec web python3 manage.py createsuperuser 
```
- Соберите статику
```sh
docker-compose exec web python manage.py collectstatic --no-input 
```
- Запустятся контейнеры, сайт будет доступен по адресу http://localhost/
- Спецификация API будет доступна http://localhost/redoc/

## Системные требования:
- [Python](https://www.python.org/) 3.10.4
- [PostgreSQL](https://www.postgresql.org/) 13
- [Docker](https://www.docker.com/) 4.10.1
- [Docker Compose](https://docs.docker.com/compose/) 3.8

## Планы по доработке:
>Проект сделан в учебных целях, доработка не планируется.

## Используемые технологии:
- [Django](https://www.djangoproject.com/) 2.2.16
- [Django REST framework](https://www.django-rest-framework.org/) 3.12.4
- [django-filter](https://pypi.org/project/django-filter/) 21.1
- [djoser](https://djoser.readthedocs.io/en/latest/getting_started.html) 2.1.0
- [python-dotenv](https://pypi.org/project/python-dotenv/) 0.20.0
- [Nginx](https://nginx.org/ru/) 1.21.3

## Авторы:
- [Michail Spiridonov](https://github.com/Muxa2793)
- [Denis Shahbazyan](https://github.com/DenisShahbazyan)
- [Alisa Gafarova](https://github.com/alisagafarova)

## Лицензия:
- MIT
