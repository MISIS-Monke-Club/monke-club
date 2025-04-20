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
  "username": str,
  "email": str,
  "password": str
  "password2": str
}
```

```html
Пример успешного ответа (201 Created)
{
  "message": "User successfully registered",
  "user": {
    "id": 2,
    "username": str,
    "email": str,
    "is_active": bool
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
  "refresh": str,
  "access":  str
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
  "username": str,
  "full_name": str,
  "rating": float,
  "photo": str | null,
  "course": int,
  "faculty": str | null,
  "social_networks": [
    {
      "name": "tg",
      "text": "alex_topand"
    },
    {
      "name": "vk",
      "text": "sosi_bibu"
    }
  ] | []
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
  "faculty": "test",
  "full_name": "Alex Topand"
}
```
Пример успешного ответа (200 OK)
```html
{
  "username": "Topand",
  "full_name": " ",
  "rating": 5.0,
  "photo": str | null,
  "course": 2,
  "faculty": str | null,
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
    "full_name": str
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
еще поиск параметр search

#### Пример запроса с сортировкой

```http
GET http://localhost:3000/api/v1/marketplace/mentors/?ordering=-rating&subjects=test3,test4 HTTP/1.1
Host: localhost:3000
```
Ответ
```html
[
    {
        "username": str",
        "full_name": str | "",
        "services": [] | [1,2],
        "subjects": [] | [1,2],
        "rating": float,
        "photo": str | null,
        "count_successful_transactions": int
    },
    {
        "username": "tuntun_user1",
        "full_name": "",
        "services": [],
        "subjects": [],
        "rating": 5.0,
        "photo": null,
        "count_successful_transactions": 5
    }
]
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
    "username": str",
    "full_name": str;
    "description": str,
    "services": [
        {
            "id": 1,
            "name": "test"
        }
    ] | [],
    "rating": int,
    "photo": str | null,
    "subjects": [
        {
            "id": 1,
            "name": "test3"
        }
    ] | [],
    "count_successful_transactions": int,
    "social_network": [
        {
            "name": "tg",
            "text": "alex_topand"
        },
        {
            "name": "vk",
            "text": "sosi_bibu"
        }
    ] | [],
    "course": int,
    "faculty": str | null;
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
  "description": str,
  "count_successful_transactions": int
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
    "name": str
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
        "name": str
    },
    {
        "id": 2,
        "name": "test4"
    }
]
```


## Marketplace Applications

### Get Filter Fields
**Endpoint**: `GET /api/v1/marketplace/applications/filter-fields/`  
**Response**:
```json
{
    "fields": {
        "subjects": "Предметы",
        "services": "Тип задачи",
        "year": "Курс",
        "is_free": "Бесплатно"
    }
}
```

### Get Ordering Fields
**Endpoint**: `GET /api/v1/marketplace/applications/ordering-fields/`  
**Response**:
```json
{
    "ordering_fields": [
        "date_of_creation",
        "price"
    ]
}
```

### List/Create Applications
**Endpoint**: `GET/POST /api/v1/marketplace/applications/`  
**GET Response**:
```json
[
    {
        "name": "Помощь с Python проектом",
        "username": "tuntun_user1",
        "year": 3,
        "subjects": [],
        "services": [],
        "date_of_creation": "2025-04-20",
        "price": "2500.00",
        "slug": "pomoshch-s-python-proektom"
    }
]
```

**POST Request**:
```json
{
    "id": 3,
    "name": "Testname",
    "slug": "testname",
    "date_of_creation": "2025-04-19",
    "description": "Testdesc",
    "price": "1000.00",
    "is_finished": false,
    "year": 4,
    "file": null,
    "user": 1,
    "executor_id": 2
}
```

### Application Detail
**Endpoint**: `GET/PUT/PATCH/DELETE /api/v1/marketplace/applications/{slug}/`  
**GET Response**:
```json
{
    "id": 1,
    "services": [],
    "subjects": [],
    "name": "Помощь с Python проектом",
    "slug": "pomoshch-s-python-proektom",
    "date_of_creation": "2025-04-20",
    "description": "Нужно помочь с проектом по Django",
    "price": "2500.00",
    "is_finished": false,
    "year": 3,
    "file": null,
    "user": 1,
    "executor_id": null
}
```

**PUT/PATCH Request**:
```json
{
    "id": 4,
    "name": "test",
    "slug": "test",
    "date_of_creation": null,
    "description": "esd",
    "price": "1.00",
    "is_finished": false,
    "year": 1,
    "file": null,
    "user": 1,
    "executor_id": null,
    "services": [1],
    "subjects": [1,2]
}
```

---

## Events

### Get Event Types
**Endpoint**: `GET /api/v1/events/event-types/`  
**Response**: `[]`

### Get Filter Fields
**Endpoint**: `GET /api/v1/events/filter-fields/`  
**Response**:
```json
{
    "fields": {
        "event_types": "Тип мероприятия",
        "is_free": "Бесплатно",
        "price_min": "Минимальная цена",
        "price_max": "Максимальная цена",
        "start_date": "Дата начала (ГГГГ-ММ-ДД)",
        "end_date": "Дата окончания (ГГГГ-ММ-ДД)",
        "location": "Местоположение"
    }
}
```

### Get Ordering Fields
**Endpoint**: `GET /api/v1/events/ordering-fields/`  
**Response**:
```json
{
    "ordering_fields": [
        "date",
        "-date",
        "price",
        "-price"
    ]
}
```

### List/Create Events
**Endpoint**: `GET/POST /api/v1/events/`  
**GET Response**:
```json
[
    {
        "id": 1,
        "title": "Testname",
        "date": "2025-04-20T07:13:21Z",
        "location": "Москва-Сити",
        "image": "http://localhost:3000/media/events/2025-04-17_13_Dm27uXQ.44.54.jpg"
    }
]
```

**POST Request**:
```json
{
    "title": "Test2",
    "date": "2025-04-20T07:13:21Z",
    "price": 52,
    "location": "String",
    "description": "string",
    "registration_link": "https://testurl.com",
    "event_type": 1,
    "image": null
}
```

### Event Detail
**Endpoint**: `GET/PUT/PATCH/DELETE /api/v1/events/{slug}/`  
**GET Response**:
```json
{
    "id": 3,
    "title": "weewe",
    "date": "2025-04-20T07:22:46Z",
    "price": 1000,
    "location": "112112",
    "description": "2121fwdedqd",
    "registration_link": "https://altushkimoskvi.ru",
    "event_type": {
        "type_name": "Test"
    },
    "image": "http://localhost:3000/media/events/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-04-19_%D0%B2_22.07.42.png",
    "slug": "weewe"
}
```

**PUT/PATCH Request**:
```json
{
    "title": "weewe",
    "date": "2025-04-20T07:22:46Z",
    "price": 1000,
    "location": "112112",
    "description": "2121fwdedqd",
    "registration_link": "https://altushkimoskvi.ru",
    "event_type": 1,
    "image": "http://localhost:3000/media/events/%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA_%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0_2025-04-19_%D0%B2_22.07.42.png"
}
```

---

### Notes:
- Все даты в формате ISO 8601: `ГГГГ-ММ-ДД`
- Поля `slug` генерируются автоматически на основе названия
- Для файловых полей (`file`, `image`) ожидается URL после загрузки