from django.db import migrations
from django.utils import timezone
from django.utils.text import slugify
from unidecode import unidecode

def create_mock_applications(apps, schema_editor):
    User = apps.get_model("auth", "User")
    Application = apps.get_model("marketplace", "Application")
    Service = apps.get_model("marketplace", "Service")
    Subject = apps.get_model("marketplace", "Subject")

    users = User.objects.filter(username__in=["tuntun_user1", "tuntun_user2"])

    # Создаём необходимые Service и Subject, если их нет
    services = {service.id: service for service in Service.objects.all()}
    subjects = {subject.id: subject for subject in Subject.objects.all()}

    mock_applications_data = [
        {
            "user": "tuntun_user1",
            "name": "Помощь с Python проектом",
            "description": "Нужно помочь с проектом по Django",
            "price": 2500.00,
            "year": 3,
            "is_finished": False,
            "services": [1, 2],
            "subjects": [2, 1],
        },
        {
            "user": "tuntun_user2",
            "name": "Решение задач по алгебре",
            "description": "Срочно решить 5 задач по алгебре",
            "price": 1500.00,
            "year": 2,
            "is_finished": True,
            "services": [3],
            "subjects": [3],
        },
    ]

    # Прежде чем использовать, проверим наличие всех необходимых предметов и сервисов
    for data in mock_applications_data:
        user = users.get(username=data["user"])

        # Проверяем, существуют ли все предметы и сервисы
        app_services = []
        for service_id in data["services"]:
            if service_id not in services:
                # Создаём сервис, не указывая id
                services[service_id] = Service.objects.create(name=f"Service {service_id}")
            app_services.append(services[service_id].id)  # Добавляем ID, а не объект

        app_subjects = []
        for subject_id in data["subjects"]:
            if subject_id not in subjects:
                # Создаём предмет, не указывая id
                subjects[subject_id] = Subject.objects.create(name=f"Subject {subject_id}")
            app_subjects.append(subjects[subject_id].id)  # Добавляем ID, а не объект

        slug_base = slugify(unidecode(data["name"]))
        unique_slug = slug_base
        counter = 1

        while Application.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{slug_base}-{counter}"
            counter += 1

        # Создание заявки
        app = Application.objects.create(
            user=user,
            name=data["name"],
            description=data["description"],
            price=data["price"],
            year=data["year"],
            is_finished=data["is_finished"],
            date_of_creation=timezone.now(),
            slug=unique_slug,
        )

        # Добавляем сервисы и предметы через ManyToMany, передаем ID
        app.services.set(app_services)
        app.subjects.set(app_subjects)
        app.save()


class Migration(migrations.Migration):

    dependencies = [
        ("marketplace", "0002_application"),
        ("user", "0004_create_mock_user"),
        ("auth", "0012_alter_user_first_name_max_length"),
        ("sessions", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_mock_applications),
    ]