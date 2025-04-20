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

### 🔹 Обновление access-токена

**Метод:** `POST`  
**URL:** `/api/v1/token/refresh/`  

**Описание:**  
Позволяет получить новый access-токен, используя ранее выданный refresh-токен.  
Необходим для продления сессии пользователя без повторного ввода логина и пароля.

---

#### Параметры тела запроса (JSON)

| Поле      | Тип    | Обязательное | Описание                            |
|-----------|--------|--------------|-------------------------------------|
| `refresh` | string | да           | Refresh-токен, полученный при входе |

---

#### Пример запроса

```http
POST /api/v1/token/refresh/ HTTP/1.1
Host: localhost:3000
Content-Type: application/json

{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0NzY5NjY5OCwiaWF0IjoxNzQ1MTA0Njk4LCJqdGkiOiIzMGI2MzRmMDY5ZWI0MTA3ODQxMmRmNTk3NTU4MTk2ZSIsInVzZXJfaWQiOjJ9.i6GPaZD2wFAl0W8-ElR0MvuNSkIWrPGGHuVvZa4xVRM"
}
```

Пример успешного ответа (200 OK)
```html
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ1NzE0NTQ4LCJpYXQiOjE3NDUxMDk3MjksImp0aSI6ImViM2RiMWU0OGEyMzQ4NmNiMTc3OWU5NDM0N2Q1Nzk4IiwidXNlcl9pZCI6NX0.eqYJpbkA63x-TwNuwSw9d0bqJpBDry47G8sE-8QNNdU"
}
```



### 🔹 Проверка токена (verify)

**Метод:** `POST`  
**URL:** `/api/v1/token/verify/`  

**Описание:**  
Проверяет валидность переданного JWT-токена. Используется для подтверждения, что токен не просрочен и не подделан.  
Если токен действителен — возвращается пустой ответ с кодом 200. Если недействителен — ошибка 401.

---

#### Параметры тела запроса (JSON)

| Поле    | Тип    | Обязательное | Описание                      |
|---------|--------|--------------|-------------------------------|
| `token` | string | да           | JWT access- или refresh-токен |

---

#### Пример запроса

```http
POST /api/v1/token/verify/ HTTP/1.1
Host: localhost:3000
Content-Type: application/json

{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ1NzA5NDk4LCJpYXQiOjE3NDUxMDQ2OTgsImp0aSI6IjIzMjdkMGY4ZTBhNzRjYmNiZTg2YzgxMWJhYjc1OWEwIiwidXNlcl9pZCI6Mn0.v5p_2wr4F7N_SYTfDtXeuR3eCS671WzLl0g1tc5Q_cU"
}
```

Пример успешного ответа (200 OK)
```html
{}
```

### 🔹 Получение профиля пользователя

**Метод:** `GET`  
**URL:** `/api/v1/profile/{username}/`  

**Описание:**  
Возвращает публичный профиль пользователя по его `username`.  
Полезно для отображения информации о пользователе, например, на странице профиля.

---

#### Параметры URL

| Параметр   | Тип     | Обязательный | Описание                      |
|------------|---------|--------------|-------------------------------|
| `username` | string  | да           | Уникальное имя пользователя   |

---

#### Пример запроса

```http
GET /api/v1/profile/Topand/ HTTP/1.1
Host: localhost:3000
```
Пример успешного ответа (200 OK)
```html
{
  "username": "Topand",
  "full_name": " ",
  "rating": 5.0,
  "photo": null,
  "course": 2,
  "faculty": "fsdf",
  "social_networks": [
    {
      "name": "tg",
      "text": "alex_topand"
    },
    {
      "name": "vk",
      "text": "sosi_bibu"
    }
  ]
}
```


### 🔹 Обновление профиля пользователя

**Метод:** `PUT`  
**URL:** `/api/v1/profile/{username}/`  

**Описание:**  
Позволяет обновить информацию в профиле пользователя — факультет, ссылки на социальные сети и другие поля.  
🔐 Требуется авторизация. Только владелец профиля может вносить изменения.

---

#### Заголовки

| Заголовок         | Значение                          |
|-------------------|-----------------------------------|
| `Authorization`   | `Bearer <access_token>`           |

---

#### Параметры URL

| Параметр   | Тип     | Обязательный | Описание                    |
|------------|---------|--------------|-----------------------------|
| `username` | string  | да           | Уникальное имя пользователя |

---

#### Параметры тела запроса (JSON)

| Поле             | Тип              | Обязательное | Описание                              |
|------------------|------------------|--------------|---------------------------------------|
| `social_networks`| array of objects | нет          | Ссылки на соцсети (`name`, `text`)    |
| `faculty`        | string           | нет          | Название факультета                   |
| другие поля      | —                | —            | Можно передавать и другие доступные поля |

---

#### Пример запроса

```http
PUT /api/v1/profile/Topand/ HTTP/1.1
Host: localhost:3000
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6...
Content-Type: application/json

{
  "social_networks": [
    {
      "name": "tg",
      "text": "alex_topand"
    },
    {
      "name": "vk",
      "text": "sosi_bibu"
    }
  ],
  "faculty": "test"
}
```
Пример успешного ответа (200 OK)
```html
{
  "username": "Topand",
  "full_name": " ",
  "rating": 5.0,
  "photo": null,
  "course": 2,
  "faculty": "test",
  "social_networks": [
    {
      "name": "tg",
      "text": "alex_topand"
    },
    {
      "name": "vk",
      "text": "sosi_bibu"
    }
  ]
}
```

## Marketplace

### 🔹 Список менторов (маркетплейс)

**Метод:** `GET`  
**URL:** `/api/v1/marketplace/mentors/`  

**Описание:**  
Возвращает список всех менторов, доступных в маркетплейсе. Поддерживает фильтрацию и сортировку по рейтингу и количеству успешных сделок.  
Доступно без авторизации.

---

#### Параметры запроса (Query params)

| Параметр      | Тип     | Описание                                                                 |
|---------------|---------|--------------------------------------------------------------------------|
| `ordering`    | string  | Сортировка. Доступные значения:                                         |
|               |         | `count_successful_transactions` — по возрастанию успешных сделок         |
|               |         | `-count_successful_transactions` — по убыванию успешных сделок *(по умолчанию)* |
|               |         | `rating` — по возрастанию рейтинга                                      |
|               |         | `-rating` — по убыванию рейтинга  <br/>http://localhost:3000/api/v1/marketplace/mentors/ordering-fields/                                      |
| Другие фильтры| —       | Зависит от реализации `MentorFilters`. См. `GET /api/v1/marketplace/mentors/filters/` |

---

#### Пример запроса с сортировкой

```http
GET http://localhost:3000/api/v1/marketplace/mentors/?ordering=-rating&subjects=test3,test4 HTTP/1.1
Host: localhost:3000
```


### 🔹 Создание профиля ментора

**Метод:** `POST`  
**URL:** `/api/v1/marketplace/mentors/`  

**Описание:**  
Создаёт профиль ментора, связанный с текущим авторизованным пользователем.  
🔐 Требуется авторизация.

---

#### Заголовки

| Заголовок       | Значение                 |
|-----------------|--------------------------|
| `Authorization` | `Bearer <access_token>`  |

---

#### Параметры тела запроса (JSON)

| Поле                        | Тип               | Обязательное | Описание                                             |
|-----------------------------|-------------------|--------------|------------------------------------------------------|
| `services`                  | array of integer  | нет          | Список ID услуг, предоставляемых ментором            |
| `subjects`                  | array of integer  | нет          | Список ID предметов, в которых ментор специализируется |
| `description`               | string            | нет          | Описание ментора                                     |

---

#### Пример запроса

```http
POST /api/v1/marketplace/mentors/ HTTP/1.1
Host: localhost:3000
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6...
Content-Type: application/json

{
}

{
    "services": [1]
}
```
Ответ 200
```html
{
    "services": [],
    "subjects": [],
    "description": "",
    "count_successful_transactions": 0
}
```

### 🔹 Детальный профиль ментора

**Метод:** `GET`  
**URL:** `/api/v1/marketplace/mentors/{username}/`  

**Описание:**  
Возвращает подробную информацию о менторе по его `username`.  
Доступно без авторизации.

---

#### Параметры URL

| Параметр   | Тип     | Обязательный | Описание                    |
|------------|---------|--------------|-----------------------------|
| `username` | string  | да           | Уникальное имя пользователя ментора |

---

#### Пример запроса

```http
GET /api/v1/marketplace/mentors/Topand/ HTTP/1.1
Host: localhost:3000

```
Пример успешного ответа (200 OK)
```html
{
    "username": "Topand",
    "full_name": "",
    "description": "",
    "services": [
        {
            "id": 1,
            "name": "test"
        }
    ],
    "rating": 5.0,
    "photo": null,
    "subjects": [
        {
            "id": 1,
            "name": "test3"
        }
    ],
    "count_successful_transactions": 0,
    "social_network": [
        {
            "name": "tg",
            "text": "alex_topand"
        },
        {
            "name": "vk",
            "text": "sosi_bibu"
        }
    ],
    "course": 2,
    "faculty": "test"
}
```

### 🔹 Обновление профиля ментора

**Метод:** `PUT`  
**URL:** `/api/v1/marketplace/mentors/{username}/`  

**Описание:**  
Позволяет владельцу профиля ментора обновить данные: список предметов, услуг, описание и другие поля.  
🔐 Требуется авторизация. Только сам ментор может редактировать свой профиль.

---

#### Заголовки

| Заголовок       | Значение                 |
|-----------------|--------------------------|
| `Authorization` | `Bearer <access_token>`  |

---

#### Параметры URL

| Параметр   | Тип     | Обязательный | Описание                            |
|------------|---------|--------------|-------------------------------------|
| `username` | string  | да           | Уникальное имя пользователя ментора |

---

#### Параметры тела запроса (JSON)

| Поле                        | Тип              | Обязательное | Описание                                |
|-----------------------------|------------------|--------------|-----------------------------------------|
| `services`                  | array of integer | нет          | Список ID предоставляемых услуг         |
| `subjects`                  | array of integer | нет          | Список ID предметов                     |
| `description`               | string           | нет          | Описание ментора                        |

---

#### Пример запроса

```http
PUT /api/v1/marketplace/mentors/Topand/ HTTP/1.1
Host: localhost:3000
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6...
Content-Type: application/json

{
  "subjects": [1]
}
```
Пример успешного ответа (200 OK)

```html
{
  "services": [1],
  "subjects": [1],
  "description": "",
  "count_successful_transactions": 0
}
```


### 🔹 Список услуг (Services)

**Метод:** `GET`  
**URL:** `/api/v1/marketplace/services/`  

**Описание:**  
Возвращает список всех услуг, доступных в системе.  
Доступно без авторизации. Используется, например, при создании или редактировании профиля ментора.

---

#### Пример запроса

```http
GET /api/v1/marketplace/services/ HTTP/1.1
Host: localhost:3000
```

Ответ 200
```html
[
  {
    "id": 1,
    "name": "test"
  },
  {
    "id": 2,
    "name": "test2"
  }
]
```


### 🔹 Список предметов (Subjects)

**Метод:** `GET`  
**URL:** `/api/v1/marketplace/subjects/`  

**Описание:**  
Возвращает список всех предметов, доступных в системе.  
Доступно без авторизации. Используется, например, при создании или редактировании профиля ментора.

---

#### Пример запроса

```http
GET /api/v1/marketplace/subjects/ HTTP/1.1
Host: localhost:3000
```

Ответ 200
```html
[
    {
        "id": 1,
        "name": "test3"
    },
    {
        "id": 2,
        "name": "test4"
    }
]
```