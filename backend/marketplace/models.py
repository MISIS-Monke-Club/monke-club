from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название предмета")

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название предмета")

    def __str__(self):
        return self.name
