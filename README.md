# vsnder

## Запуск
- Делаем .env файл с ключами: REDIS_USER, REDIS_PASSWORD
- Делаем /services/server/db.env файл с ключами: DB_HOST, DB_DATABASE, DB_USER, DB_PASSWORD, REDIS_USER, REDIS_PASSWORD, REDIS_DOMAIN, REDIS_PORT
- (когда-нибудь окружение будет сделано по лучше, но пока живем так)
- docker-compose up -d --build

Сервис будет доступен по http://localhost

Есть swagger по адресу http://localhost/swagger. Там описаны все открытые ручки, а также DTO (data transfer object) - формат отдачи/передачи данных с ними.

## Важно
При локальном запуске развернется контейнер с БД, миграции накатятся автоматически. После первого запуска нужно будет зайти в контейнер сервера и выполнить команды:
```
cd app
pdm run python insert_users_to_db.py
```
Будут созданы все пустые пользователи с паролем 12345678
