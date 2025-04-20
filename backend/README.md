
# 📄 Application API

API для управления заявками (Application) пользователей. Поддерживаются операции создания, получения списка, обновления и удаления заявок.

## 🔧 1. Создание заявки

**Endpoint:** `POST http://localhost:3000/marketplace/applications/`  
**Описание:** Создание новой заявки.

### 🔹 Пример запроса

```json
{
    "subjects": [],
    "services": [],
    "name": "",
    "date_of_creation": null,
    "description": "",
    "price": null,
    "is_finished": false,
    "year": null,
    "user": null,
    "executor_id": null
}



📋 2. Получение списка заявок

Endpoint: `GET http://localhost:3000/marketplace/applications/`
Описание: Получение всех заявок текущего пользователя.

🔹 Пример ответа

[
    {
        "name": "Заявка без названия12",
        "username": "root",
        "year": 5,
        "subjects": [
            {
                "id": 1,
                "name": "test предмет"
            }
        ],
        "services": [
            {
                "id": 1,
                "name": "тест предмет"
            }
        ],
        "date_of_creation": "2025-04-19",
        "price": "1000.00"
    }
]



⸻

✏️ 3. Обновление заявки

Endpoint: PUT/PATCH http://localhost:3000/marketplace/applications/{slug}/
Описание: Полное или частичное обновление заявки.

🔹 Проблемный пример

{
  "name": "Срочная помощь с диффурами",
  "year": 2,
  "subjects": [5, 6],
  "services": [7],
  "description": "Нужно к завтрашнему дню",
  "price": "2000.00",
  "is_finished": false
}

⸻

🗑️ 4. Удаление заявки

Endpoint: DELETE http://localhost:3000/marketplace/applications/{slug}/
Описание: Удаление существующей заявки.

Тело запроса: не требуется.

⸻

❗ Примеры ошибок

🔹 Несуществующие ID

Запрос:

{
  "name": "Тестовая заявка",
  "year": 1,
  "subjects": [999],
  "services": [888],
  "price": "500.00"
}

Ответ:

400 Bad Request
{
  "subjects": ["Выбранный объект не существует."],
  "services": ["Выбранный объект не существует."]
}



⸻

🔹 Отсутствие обязательных полей

Запрос:

{
  "year": 1,
  "price": "500.00"
}

Ответ:

400 Bad Request
{
  "name": ["Обязательное поле."],
  "subjects": ["Обязательное поле."],
  "services": ["Обязательное поле."]
}



⸻

=======
## GET /marketplace/mentors/
Массив всех менторов 
возможна сортировка
Структура ответа
```
[
    {
        "username": "test",
        "full_name": "",
        "services": [
            {
                "id": 1,
                "name": "laba"
            },
            {
                "id": 2,
                "name": "test"
            },
            {
                "id": 3,
                "name": "testr3"
            }
        ],
        "subjects": [
            {
                "id": 1,
                "name": "math"
            }
        ],
        "count_successful_transactions": 10,
        "photo": url,
        "rating": int,
    },
    {
        "username": "root",
        "full_name": "FirstName LastName",
        "services": [
            {
                "id": 2,
                "name": "test"
            },
            {
                "id": 3,
                "name": "testr3"
            }
        ],
        "subjects": [
            {
                "id": 1,
                "name": "math"
            }
        ],
        "count_successful_transactions": 0,
        "photo": url,
        "rating": int,
    }
]
```
Пояснения к полям
username 
full_name
services - лаба курсач и тд
subjects - предметы 
count_successful_transactions - количество выполненных заказов

null:
photo,
services,
subjects,

`/marketplace/mentors/?ordering=-count_successful_transactions`
можно делать сортировку
***

## GET /marketplace/mentors/ordering-fields/
все сортировки у менторов списка
Структура ответа
```
[
    {
        "value": "count_successful_transactions",
        "label": "Успешных сделок (по возрастанию)"
    },
    {
        "value": "-count_successful_transactions",
        "label": "Успешных сделок (по убыванию)"
    }
]
```
Пояснения к полям

value - Что вставлять в ordering
label - название


***

## GET /marketplace/mentors/<str: username>/
все сортировки у менторов списка
Структура ответа
```
{
    "username": "test",
    "full_name": "",
    "description": "test2",
    "services": [
        {
            "id": 1,
            "name": "laba"
        },
        {
            "id": 2,
            "name": "test"
        },
        {
            "id": 3,
            "name": "testr3"
        }
    ],
    "subjects": [
        {
            "id": 1,
            "name": "math"
        }
    ],
    "count_successful_transactions": 10,
    "photo": url,
    "rating": int,
    "social_network: [
    {
        "name": str
         "text": str
    }
    ]
    
}

```
Пояснения к полям
все тоже самое только добавляется description

null:
photo,
services,
subjects,
***

## POST api/marketplace/mentors/
все сортировки у менторов списка

Структура запроса
```json
{
  "services": [2, 1],
  "subjects": [1],
  "description": "Ментор ssss математике и физике",
  "count_successful_transactions": 0
}
```

Структура ответа
```
{
    "services": [
        1,
        2
    ],
    "subjects": [
        1
    ],
    "description": "Ментор ssss математике и физике",
    "count_successful_transactions": 0
}
```
***

## PUT api/marketplace/mentors/<str: username>
все сортировки у менторов списка

Структура запроса
```json
{
  "services": [2, 1],
  "subjects": [1],
  "description": "Ментор ssss математике и физике",
  "count_successful_transactions": 0
}
```

Структура ответа
```
{
    "services": [
        1,
        2
    ],
    "subjects": [
        1
    ],
    "description": "Ментор ssss математике и физике",
    "count_successful_transactions": 0
}
```
***

## GET marketplace/mentors/filters/
все сортировки у менторов списка


Структура ответа
```
{
    "courses": [
        3
    ],
    "subjects": [
        {
            "value": "math",
            "label": "Math"
        },
        {
            "value": "info",
            "label": "Info"
        }
    ],
    "services": [
        {
            "value": "test",
            "label": "Test"
        },
        {
            "value": "testr3",
            "label": "Testr3"
        },
        {
            "value": "laba",
            "label": "Laba"
        }
    ]
}
```
***






## GET /marketplace/services/
Массив всех сервисов
Структура ответа
```
[
    {
        "id": 1,
        "name": "Pipiska"
    },
    {
        "id": 2,
        "name": "Gondoshka"
    }
]
```



## GET /marketplace/services/
Массив всех сабжектов
Структура ответа
```
[
    {
        "id": 1,
        "name": "Bandito Bobrito"
    },
    {
        "id": 2,
        "name": "Ballerina Capichino"
    }
]
```

# CRUD Юзера
## GET /api/users/
Список всех пользователей 
Структура ответа
```
[
    {
        "id": 1,
        "username": "кщще",
        "email": "root@email.com",
        "description": "",
        "rating": "0.0",
        "course": 1,
        "faculty": ""
    }
]
```
## GET /api/users/username
Определенный пользователь
Структура ответа
```
{
    "id": 1,
    "username": "гыукт",
    "email": "root@email.com",
    "description": "",
    "photo": null,
    "rating": "0.0",
    "course": 1,
    "faculty": ""
}
```
## POST /api/users/
Определенный пользователь
Входящие данные
```
{
  "username": "new_user123",
  "email": "new_user123123@example.com",
  "password": "pa123ssword123"
}
```
Структура ответа
```
{
    "id": 2,
    "username": "new_user123",
    "email": "new_user123123@example.com"
}
```
## PUT /api/users/username
Изменение пользователя
Входящие данные (издеваемся над new_user123)
```
{
    "username": "USER_GAy",
    "email": "new_user123123@example.com",
    "description": null,
    "photo": null,
    "rating": "5.0",
    "course": 1,
    "faculty": null
}
```
Структура ответа
```
{
    "id": 2,
    "username": "USER_GAy",
    "email": "new_user123123@example.com",
    "description": null,
    "rating": "5.0",
    "course": 1,
    "faculty": null
}
```
## PATCH /api/users/username
Изменение пользователя
Входные данные
```
{
    "username": "USER_NE_GAy",
    "email": "USER_NE_GAy123123@example.com",
    "description": null,
    "photo": null,
    "rating": "2.0",
    "course": 3,
    "faculty": null
}
```
Структура ответа
```
{
    "id": 2,
    "username": "USER_NE_GAy",
    "email": "USER_NE_GAy123123@example.com",
    "description": null,
    "rating": "2.0",
    "course": 3,
    "faculty": null
}
```
## DELETE /api/users/username
Входные данные

```
{
    "username": "USER_NE_GAy",
    "email": "USER_NE_GAy123123@example.com",
    "description": null,
    "photo": null,
    "rating": "2.0",
    "course": 3,
    "faculty": null
}
```
204 - все ок


## GET /api/v1/vacancies/
Тип ответа
```
 {
        "title": "аываыв",
        "price": null,
        "work_type": {
            "title": "еуые"
        },
        "job_experience": null
    },
    {
        "title": "тест",
        "price": null,
        "work_type": {
            "title": "еуые"
        },
        "job_experience": null
    }
```
work_type - тип работы (удаленка, ...)
job_experience - опыт работы
все может быть null кроме title description


## GET /api/v1/vacancies/<slug:slug>/
Тип ответа
```
 {
    "title": "тест",
    "description": "авыа",
    "stack": [
        {
            "title": "test"
        },
        {
            "title": "tewst3"
        }
    ],
    "data_created": "21:46 19 Apr 2025",
    "data_end": null,
    "schedule": null,
    "work_space": null,
    "price": null,
    "work_type": {
        "title": "еуые"
    },
    "job_experience": null
}
```

## POSR /api/v1/vacancies/<slug:slug>/
Тип ответа
```
 {
    "title": "fffff",
    "description": "21312312",
    "stack": [
        1
    ],
    "data_created": "22:22 19 Apr 2025",
    "data_end": null,
    "schedule": null,
    "work_space": null,
    "price": null,
    "work_type": 3,
    "job_experience": null
}

```

Тип запроса
```json
{
 "title": "fffff",
 "description": "21312312",
 "stack": [1],
 "work_type": 3
}
```
