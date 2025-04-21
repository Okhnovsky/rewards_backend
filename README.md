# REWARDS BACKEND

## О проекте

Представляет собой бэкенд приложения для назначения запланированных наград.


## Стек технологий
- Python 3
- Django 5
- Django Rest Framework
- PostgreSQL
- Docker
- Daphne
- Nginx
- Celery
- Redis (message brocker and result backend)


## Едпоинты
- POST /api/token/
- POST /api/token/refresh/
- POST /api/token/verify/
- GET /api/profile/
- GET /api/rewards/
- POST /api/rewards/request/

- /admin
- /schema/
- /schema/swagger-ui/

Подробное описание методов можно посмотреть в SWAGGER после запуска проекта (127.0.0.1/schema/swagger-ui/). Для входа необходимо будет ввести логин и пароль. Доступно только администраторам.

## Запуск проекта
- Клонируем репозиторий
```
git clone git@github.com:Okhnovsky/rewards_backend.git
```
- Переходим в появившуюся директорию rewards_backend/
```
cd rewards_backend
```
- В данной директории создаем файл .env со следующими переменными:
```
SECRET_KEY='django-insecure-j5#hn+(r%_90+lrcua9w1866w^1!@4(&c@$+1wpz6iij7_7vo#'
DB_NAME='postgres'
POSTGRES_USER='postgres'
POSTGRES_PASSWORD='postgres'
DB_HOST='db'
DB_PORT='5432'
CELERY_BROKER_URL='redis://redis_brocker:6379/0'
```
- Запускаем контейнеры docker compose
```
docker compose up -d
```
- Применяем миграции, создаем суперпользователя, собираем статику:
```
docker compose exec rewards_backend python manage.py migrate
docker compose exec rewards_backend python manage.py createsuperuser
docker compose exec rewards_backend python manage.py collectstatic --no-input
```
- Запускаем celery воркер в контейнере rewards_backend:
```
docker compose exec rewards_backend celery -A rewards_backend worker -l INFO --detach
```
- Перехоим в административную панель http://127.0.0.1/admin/
