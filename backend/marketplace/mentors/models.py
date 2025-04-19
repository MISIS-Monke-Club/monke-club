from django.contrib.auth.models import User
from django.db import models


class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    services = models.ManyToManyField("marketplace.service", blank=True)
    subjects = models.ManyToManyField("marketplace.subject", blank=True)
    description = models.TextField(blank=True)
    count_successful_transactions = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
