from django.db import models
from django.contrib.auth.models import User


class UserBio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="bio")
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    rating = models.DecimalField(max_digits=5, decimal_places=1, default=0.0)
    course = models.PositiveIntegerField(default=1)
    faculty = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username


class SocialNetwork(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()
    user = models.ForeignKey(
        UserBio, related_name="social_networks", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.name} - {self.text}"


class UserRatingActivity(models.Model):
    ACTIVITY_CHOICES = [
        ("account_created", "Создание аккаунта"),
        ("filled_description", "Заполнено описание"),
        ("filled_full_name", "Заполнено ФИО"),
        ("added_socials", "Добавлены соцсети"),
        ("linked_subjects", "Добавлены предметы"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rating_activities")
    activity_type = models.CharField(max_length=50, choices=ACTIVITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "activity_type")