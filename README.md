# vsnder

## Запуск
- docker-compose up -d --build

После запуска сервис будет доступен по http://localhost

```
Фронт и бек доступны по одному адресу, прокси раскидывает реквесты по необходимости. 
Дополнительно поднят Redis для работы с сессиями (там допом хранится user_id)
```

```
У сервера есть следующие ручки:
- POST /api/user/login
- GET /api/user/logout
- POST /api/user/edit
- POST /api/user/change_password
- GET /api/users
- GET /api/users/<user_id:int>

Доступ ко всем ручкам кроме логина осуществляется только при наличии авторизированной сессии
```

```
У клиента страницы:
- /login
- /logout (страницы нет, очистка localStorage и редирект на /login)
- /users
- /users/<user_id:int>
- /edit
- /changePassword
```
