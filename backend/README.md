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






