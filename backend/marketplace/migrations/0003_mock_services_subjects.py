from django.db import migrations


def create_mock_services_and_subjects(apps, schema_editor):
    Service = apps.get_model("marketplace", "Service")
    Subject = apps.get_model("marketplace", "Subject")

    mock_services = [
        "Консультация по Python",
        "Помощь с Django",
        "Code review",
        "Подготовка к собеседованию",
    ]

    mock_subjects = ["Алгоритмы", "Базы данных", "Frontend", "DevOps"]

    for service_name in mock_services:
        Service.objects.create(name=service_name)

    for subject_name in mock_subjects:
        Subject.objects.create(name=subject_name)


class Migration(migrations.Migration):

    dependencies = [
        ("marketplace", "0002_application"),  # или последняя твоя актуальная миграция
    ]

    operations = [
        migrations.RunPython(create_mock_services_and_subjects),
    ]
