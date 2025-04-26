### Пояснение
Это мой первый API на LiteStar, до этого делал на FastAPI. 
Потратил на исследование библиотеки и написание кода около 7-8 часов

Не стал делать аутентификацию и авторизацию, потому что забыл если честно. Надеюсь это не станет большим минусом, ведь в тестовом важно показать общий подход, да?))

# User API

REST API на базе LiteStar с CRUD-операциями для таблицы user в PostgreSQL.

## Технологии

- Backend: LiteStar (версия 2.x)
- База данных: PostgreSQL + Advanced-SQLAlchemy
- Инфраструктура: Docker
- Пакетный менеджер: Poetry 1.8.3

## Функциональность

- Создание пользователя
- Получение списка пользователей
- Получение данных одного пользователя
- Обновление данных пользователя
- Удаление пользователя
- Swagger документация

## Запуск приложения

### С использованием Docker

```bash
# Клонировать репозиторий
git clone https://github.com/vollodin61/TestLiteStarAPI
cd TestLiteStarAPI

# Запустить приложение с помощью Docker Compose
docker-compose up -d --build
```

## API Endpoints

- `GET /users` - Получить список всех пользователей
- `GET /users/{user_id}` - Получить пользователя по ID
- `POST /users` - Создать нового пользователя
- `PUT /users/{user_id}` - Обновить пользователя
- `DELETE /users/{user_id}` - Удалить пользователя

## Документация API

После запуска приложения, документация Swagger доступна по адресу:

```
http://localhost:8000/schema
http://localhost:8000/schema/swagger
http://localhost:8000/schema/elements
http://localhost:8000/schema/rapidoc
```