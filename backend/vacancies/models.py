from django.contrib.auth.models import User
from django.db import models
from slugify import slugify

class Vacancy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255, verbose_name="Название")
    slug = models.SlugField(max_length=255, blank=True, unique=True, verbose_name="Слаг")
    description = models.TextField(verbose_name="Описание")
    stack = models.ManyToManyField('Stack', related_name='vacancies', null=True, blank=True, verbose_name="Стек разработки")
    data_created = models.DateTimeField(auto_now_add=True)
    data_end = models.DateField(null=True, blank=True, verbose_name="Дата окончания")
    price = models.PositiveIntegerField(null=True, blank=True, verbose_name="Цена")
    work_type = models.ForeignKey("WorkType", related_name='vacancies', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Тип работы")
    job_experience = models.PositiveIntegerField(null=True, blank=True, verbose_name="Опыт работы")
    schedule = models.CharField(max_length=255, null=True, blank=True, verbose_name="График работы")
    work_space = models.CharField(max_length=255, null=True, blank=True, verbose_name="Место работы")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug or self.slug == "":
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class WorkType(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Stack(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return self.title