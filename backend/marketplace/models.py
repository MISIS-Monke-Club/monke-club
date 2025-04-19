from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название предмета")


class Subject(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название предмета")
