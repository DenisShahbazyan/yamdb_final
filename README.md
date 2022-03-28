![example workflow](https://github.com/DenisShahbazyan/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

### Описание: 

Групповой проект курса "Python-разработчик плюс" 

### Авторы: 

<a href="https://github.com/Muxa2793">Michail Spiridonov</a> 

    · 

<a href="https://github.com/DenisShahbazyan">Denis Shahbazyan</a> 

    · 

<a href="https://github.com/alisagafarova">Alisa Gafarova</a> 

### Установка 

Склонируйте проект на Ваш компьютер 

   ```sh 

   git clone https://github.com/DenisShahbazyan/infra_sp2.git 

   ``` 

Перейдите в папку с проектом 

   ```sh 

   cd api_yamdb 

   ``` 

Активируйте виртуальное окружение 

   ```sh 

   python3 -m venv venv 

   ``` 

   ```sh 

   source venv/bin/activate 

   ``` 

Обновите менеджер пакетов (pip) 

   ```sh 

   pip3 install --upgrade pip 

   ``` 

Установите необходимые зависимости 

   ```sh 

   pip3 install -r requirements.txt 

   ``` 

    

Запустите docker-compose 

  ```sh 

  #все команды docker-compose выполнять в папке с docker-compose.yaml 

  docker-compose up 

  ``` 

Выполните миграции 

   ```sh 

   docker-compose exec web python3 manage.py makemigrations 

   ``` 

   ```sh 

   docker-compose exec web python3 manage.py migrate 

   ``` 

Создайте пользователя с правами администратора 

   ```sh 

   docker-compose exec web python3 manage.py createsuperuser 

   ``` 

### Примеры: 

Примеры запросов можно посмотреть в документации после запуска dev-сервера: 

 

``` 

GET http://127.0.0.1:8000/redoc/ 

``` 