from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify
from unidecode import unidecode


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
        default="Заявка без названия", blank=False, verbose_name="Название заявки",unique=True
    )
    slug = models.SlugField(verbose_name="Символьный код", blank=True, unique=True)

    subjects = models.ManyToManyField(
        "marketplace.service", verbose_name="Теги/тег предмета", blank=True
    )
    services = models.ManyToManyField(
        "marketplace.subject", verbose_name="Теги типа задачи", blank=True
    )

    date_of_creation = models.DateField(
        verbose_name="Дата создания заявки", default=timezone.now, null=True
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

    file = models.FileField(
        upload_to='applications/',
        null=True,
        blank=True,
        verbose_name="Файл прикрепленный к заявке"
    )

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.name))
        super().save()

    def __str__(self):
        return f"{self.name}"
