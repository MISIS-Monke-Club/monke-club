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