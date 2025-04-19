from django.db import models
from marketplace.models import Subject, Service
from django.utils import timezone
from django.contrib.auth.models import User


class Application(models.Model):
    YEAR_CHOICES = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
        (6, "6"),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Юзер который создал заявку",
        related_name="application_creator",
    )
    name = models.CharField(
        default="Заявка без названия", blank=False, verbose_name="Название заявки"
    )

    subject_id = models.ManyToManyField(Subject, verbose_name="Теги/тег предмета")
    service_id = models.ManyToManyField(Service, verbose_name="Теги типа задачи")

    date_of_creation = models.DateField(
        verbose_name="Дата создания заявки", default=timezone.now
    )
    description = models.CharField(
        default="", blank=True, verbose_name="Описание заявки"
    )
    price = models.DecimalField(
        default=0,
        blank=False,
        decimal_places=2,
        max_digits=10,
        verbose_name="Предложенная цена",
    )
    is_finished = models.BooleanField(
        default=False, blank=False, verbose_name="Статус выполнения заявки"
    )

    executor_id = models.ForeignKey(
        User,
        verbose_name="Исполнитель",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="application_executor",
    )

    year = models.IntegerField(choices=YEAR_CHOICES, default=1, verbose_name="Курс")

    def __str__(self):
        return f"{self.name}"
