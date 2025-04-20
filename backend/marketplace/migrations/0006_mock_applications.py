from django.db import migrations
from django.utils import timezone
from django.utils.text import slugify
from unidecode import unidecode

def create_mock_applications(apps, schema_editor):
    User = apps.get_model("auth", "User")
    Application = apps.get_model("marketplace", "Application")
    Service = apps.get_model("marketplace", "Service")
    Subject = apps.get_model("marketplace", "Subject")

    # Получаем нужных юзеров
    users = User.objects.filter(username__in=["tuntun_user1", "tuntun_user2"])

    # Получаем все сервисы и предметы
    services = list(Service.objects.all())
    subjects = list(Subject.objects.all())

    # Моки заявок
    mock_applications_data = [
        {
            "user": "tuntun_user1",
            "name": "Помощь с Python проектом",
            "description": "Нужно помочь с проектом по Django",
            "price": 2500.00,
            "year": 3,
            "is_finished": False,
        },
        {
            "user": "tuntun_user2",
            "name": "Решение задач по алгебре",
            "description": "Срочно решить 5 задач по алгебре",
            "price": 1500.00,
            "year": 2,
            "is_finished": True,
        },
    ]

    for data in mock_applications_data:
        user = users.get(username=data["user"])
        app = Application.objects.create(
            user=user,
            name=data["name"],
            description=data["description"],
            price=data["price"],
            year=data["year"],
            is_finished=data["is_finished"],
            date_of_creation=timezone.now(),
        )
        app.slug = slugify(unidecode(app.name))
        app.save()

        # Добавляем теги если есть
        if services:
            app.services.add(*services[:2])  # Первые 2 сервиса
        if subjects:
            app.subjects.add(*subjects[:1])  # Первый предмет

        app.save()

class Migration(migrations.Migration):

    dependencies = [
        ("marketplace", "0002_application"),  # замени если другая актуальная
        ("user", "0004_create_mock_user"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.RunPython(create_mock_applications),
    ]