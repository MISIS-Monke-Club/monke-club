from django.db import migrations
from django.contrib.auth.hashers import make_password


def create_mock_users(apps, schema_editor):
    User = apps.get_model("auth", "User")
    UserBio = apps.get_model("user", "UserBio")

    mock_users = [
        {
            "username": "tuntun_user1",
            "email": "tuntun1@example.com",
            "password": "TunTunPassword123",
            "bio": {
                "description": "Первый тестовый пользователь",
                "course": 2,
                "faculty": "Информатика",
            },
        },
        {
            "username": "tuntun_user2",
            "email": "tuntun2@example.com",
            "password": "TunTunPassword456",
            "bio": {
                "description": "Второй тестовый пользователь",
                "course": 3,
                "faculty": "Математика",
            },
        },
        {
            "username": "sahur_admin",
            "email": "sahur@example.com",
            "password": "SahurAdminPass789",
            "bio": {
                "description": "Администратор системы",
                "course": 4,
                "faculty": "Администрирование",
            },
        },
    ]

    for user_data in mock_users:
        bio_data = user_data.pop("bio")
        user = User.objects.create(
            username=user_data["username"],
            email=user_data["email"],
            password=make_password(user_data["password"]),
        )

        UserBio.objects.create(
            user=user,
            description=bio_data["description"],
            course=bio_data["course"],
            faculty=bio_data["faculty"],
        )


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_alter_userbio_rating"),
    ]

    operations = [
        migrations.RunPython(create_mock_users),
    ]
