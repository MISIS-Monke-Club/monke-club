from django.db import models
from django.contrib.auth.models import User


class UserBio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
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
