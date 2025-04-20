from django.db import migrations
from django.utils import timezone
from slugify import slugify

def create_mock_vacancies(apps, schema_editor):
    User = apps.get_model("auth", "User")
    Vacancy = apps.get_model("vacancies", "Vacancy")
    WorkType = apps.get_model("vacancies", "WorkType")
    Stack = apps.get_model("vacancies", "Stack")
    users = User.objects.all()
    stacks = list(Stack.objects.all())
    work_types = list(WorkType.objects.all())

    mock_vacancies_data = [
        {
            "title": "Backend-разработчик Django",
            "description": "Ищем опытного Django разработчика для работы над крупным проектом.",
            "price": 120000,
            "job_experience": 2,
            "schedule": "Полный день",
            "work_space": "Удаленно"
        },
        {
            "title": "Frontend-разработчик React",
            "description": "Требуется Frontend-разработчик со знанием React и Next.js.",
            "price": 110000,
            "job_experience": 1,
            "schedule": "Гибкий график",
            "work_space": "Офис в Москве"
        },
    ]

    for i, data in enumerate(mock_vacancies_data):
        vacancy = Vacancy.objects.create(
            user=users[i % len(users)] if users else None,
            title=data["title"],
            description=data["description"],
            price=data["price"],
            job_experience=data["job_experience"],
            schedule=data["schedule"],
            work_space=data["work_space"],
            data_end=timezone.now().date(),
            work_type=work_types[0] if work_types else None
        )
        vacancy.slug = slugify(data["title"])
        vacancy.save()

        if stacks:
            vacancy.stack.add(*stacks[:2])

        vacancy.save()

class Migration(migrations.Migration):

    dependencies = [
        ("vacancies", "0005_vacancy_user"),  
    ]

    operations = [
        migrations.RunPython(create_mock_vacancies),
    ]