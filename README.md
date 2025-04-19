### 🔹 Регистрация нового пользователя

**Метод:** `POST`  
**URL:** `/api/v1/register/`  

**Описание:**  
Создаёт нового пользователя с указанным именем, электронной почтой и паролем. Возвращает сообщение об успешной регистрации и данные созданного пользователя (без пароля).

#### Параметры тела запроса (JSON)

| Поле       | Тип     | Обязательное | Описание                     |
|------------|---------|--------------|------------------------------|
| `username` | string  | да           | Логин пользователя, уникален |
| `email`    | string  | да           | Электронная почта            |
| `password` | string  | да           | Пароль (минимум 8 символов)  |

#### Пример запроса

```http
POST /api/v1/register/ HTTP/1.1
Host: localhost:3000
Content-Type: application/json

{
  "username": "Topand",
  "email": "topand@topand.ru",
  "password": "12345678"
}
```

```html
Пример успешного ответа (201 Created)
{
  "message": "User successfully registered",
  "user": {
    "id": 2,
    "username": "Topand",
    "email": "topand@topand.ru",
    "is_active": true
  }
}
```

***
### 🔹 Авторизация (login)

**Метод:** `POST`  
**URL:** `/api/v1/login/`  

**Описание:**  
Обменивает учётные данные пользователя на JWT-токены (`access` и `refresh`) и возвращает информацию о самом пользователе.

---

#### Параметры тела запроса (JSON)

| Поле       | Тип     | Обязательное | Описание               |
|------------|---------|--------------|------------------------|
| `username` | string  | да           | Логин пользователя     |
| `password` | string  | да           | Пароль пользователя    |

---

#### Пример запроса

```http
POST /api/v1/login/ HTTP/1.1
Host: localhost:3000
Content-Type: application/json

{
  "username": "Topand",
  "password": "12345678"
}


```
```html
Пример успешного ответа (200 OK)
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXV…",
  "access":  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVC…",
  "user": {
    "id": 2,
    "username": "Topand",
    "email": "topand@topand.ru",
    "is_active": true
  }
}
```