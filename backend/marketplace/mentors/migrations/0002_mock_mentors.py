from django.db import migrations


def create_mock_mentors(apps, schema_editor):
    User = apps.get_model("auth", "User")
    Mentor = apps.get_model("mentors", "Mentor")
    # Получаем нужных юзеров по username
    users_for_mentors = User.objects.filter(
        username__in=["tuntun_user1", "sahur_admin"]
    )

    mock_mentors_data = {
        "tuntun_user1": {
            "description": "Ментор по программированию",
            "count_successful_transactions": 5,
        },
        "sahur_admin": {
            "description": "Главный ментор по администрированию",
            "count_successful_transactions": 12,
        },
    }

    for user in users_for_mentors:
        mentor_data = mock_mentors_data.get(user.username)
        if mentor_data:
            Mentor.objects.create(
                user=user,
                description=mentor_data["description"],
                count_successful_transactions=mentor_data[
                    "count_successful_transactions"
                ],
            )


class Migration(migrations.Migration):

    dependencies = [
        ("mentors", "0001_initial"),
        ("user", "0004_create_mock_user"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.RunPython(create_mock_mentors),
    ]
