<<<<<<< Updated upstream
=======

Конечно! Вот красиво оформленный README.md файл с описанием API для работы с заявками (Application):

⸻



# 📄 Application API

API для управления заявками (Application) пользователей. Поддерживаются операции создания, получения списка, обновления и удаления заявок.

## 🔧 1. Создание заявки

**Endpoint:** `POST http://localhost:3000/api/applications/`  
**Описание:** Создание новой заявки.

### 🔹 Пример запроса

```json
{
  "name": "Помощь с курсовой работой",
  "year": 3,
  "subjects": [1, 2],       // ID объектов Service (например, "Математика", "Физика")
  "services": [3, 4],       // ID объектов Subject (например, "Консультация", "Решение задач")
  "description": "Нужна помощь с расчетами",
  "price": "1500.00",
  "is_finished": false
}



📋 2. Получение списка заявок

Endpoint: `GET http://localhost:3000/api/applications/`
Описание: Получение всех заявок текущего пользователя.

🔹 Пример ответа

[
  {
    "name": "Помощь с курсовой работой",
    "year": 3,
    "subjects": [
      {"id": 1, "name": "Математика", ...},
      {"id": 2, "name": "Физика", ...}
    ],
    "services": [
      {"id": 3, "name": "Консультация", ...},
      {"id": 4, "name": "Решение задач", ...}
    ],
    "date_of_creation": "2023-10-01",
    "price": "1500.00"
  }
]



⸻

✏️ 3. Обновление заявки

Endpoint: PUT/PATCH http://localhost:3000/api/applications/{slug}/
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

Endpoint: DELETE http://localhost:3000/api/applications/{slug}/
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

```

⸻

=======
>>>>>>> Stashed changes
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


Пояснения к полям
все тоже самое только добавляется description

null:
photo,
services,
subjects,
***
```

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