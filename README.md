# Приложение для управления информацией об автомобилях

Данное веб-приложение создано на Django и предназначено для управления информацией об автомобилях. Пользователи могут просматривать, добавлять, редактировать и удалять автомобили, а также оставлять комментарии к ним. Для выполнения действий, кроме просмотра, требуется регистрация и авторизация.


## Алгоритм запуска
1. Клонируем репозиторий
```
git clone
```
2. Запускаем Docker, переходим в папку с проектом
```
sudo docker compose up
```
3. Переходим на 
```
http://localhost:8000/
```

## Алгоритм авторизации: 
1. Регистрируем пользователя
```
POST localhost/api/auth/users/
{
    "email": "email@example.com,
    "password": "passsword"
}
```


2. Получение JWT-токена
```
POST api/auth/jwt/create/
{
    "email": "email@example.com,
    "password": "passsword"
}
```
3. Готово. Отправляем запросы так:
```
curl -X 'GET' \
  'http://127.0.0.1:8000/api/auth/users/me/' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer ВАШ ТОКЕН'
```

### При работе со swagger так и пишем
```
Bearer ВашТокен
```

## Эндпоинты для автомобилей
GET /api/cars/: Получить список всех автомобилей.

GET /api/cars/<id>/: Получить данные об определённом автомобиле.

POST /api/cars/: Добавить новый автомобиль (требуется авторизация).

PUT /api/cars/<id>/: Обновить информацию об автомобиле (доступно только владельцу).

DELETE /api/cars/<id>/: Удалить автомобиль (доступно только владельцу).

## Эндпоинты для комментариев
GET /api/cars/<id>/comments/: Получить комментарии к автомобилю.

POST /api/cars/<id>/comments/: Добавить комментарий (требуется авторизация).

## Регистрация админки
1. В контейнере с бэком вставить команду и следовать инструкциям
```
python manage.py createsuperuser
```

## Заливка тестовых данных в базу данных
```
python manage.py migrate - если не сделали миграции
python manage.py fill_db
```

## Технологии

- Python
- Django (последняя стабильная версия)
- Django REST Framework
- PostgreSQL 