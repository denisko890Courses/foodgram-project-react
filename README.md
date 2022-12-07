# Продуктовый помощник

«Продуктовый помощник». Данный сайт помогает создавать рецепты любому зарегестрированному пользователю. Пользователи могут подписываться на других пользователей, чтобы отслеживать новые рецепты. Также можно добавлять в избанные любимые рецепты. Реализована функция добавления рецепта в корзину, которая будет помогать формировать список ингредиентов для покупки.
You are Welcome!

[![Foodgram workflow](https://github.com/denisko890Courses/foodgram-project-react/actions/workflows/foodgram_workflows.yaml/badge.svg)](https://github.com/denisko890Courses/foodgram-project-react/actions/workflows/foodgram_workflows.yaml)

## Пример проекта доступен по
http://84.201.161.136/
login: test@test.ru
pass: Pass55word!

## <a name="tech">Технологии</a>

- Python 3.X
- Django 2.2.19
- Docker version 20.10.21
- docker-compose version 1.25.0
- Postgres
- DjangoRestFramework 3.12.4

## <a name="install">Как запустить проект</a>

* Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:denisko890Courses/foodgram-project-react.git
```
* Заполните .env файл в папке infra
```
DB_ENGINE=django.db.backends.postgresql # указываем, что работаем с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД (установите свой)
DB_HOST=db # название сервиса (контейнера)
DB_PORT=5432 # порт для подключения к БД
```

* Запустите docker-compose с помощью следующих команд
```
docker-compose up -d --build
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py createsuperuser
docker-compose exec backend python manage.py collectstatic --no-input
```
---
Проект будет доступен по адресу <http://localhost/>
