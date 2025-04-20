from django.db import models
from django.utils.text import slugify
from unidecode import unidecode

class EventType(models.Model):
    type_name=models.CharField(default="Тип мероприятия не указан",verbose_name="Тип мероприятия",null=False)
    def __str__(self):
        return self.type_name

class Event(models.Model):

    title = models.CharField(max_length=255, verbose_name="Название",unique=True)
    date = models.DateTimeField(verbose_name="Дата и время")
    price = models.IntegerField(null=True, verbose_name="Стоимость посещения")
    location = models.CharField(max_length=255, verbose_name="Место")
    description = models.TextField(verbose_name="Описание")
    registration_link = models.URLField(blank=True, null=True, verbose_name="Ссылка на регистрацию")
    event_type = models.ForeignKey(EventType,default="Тип мероприятия не указан",on_delete=models.SET_DEFAULT)
    image = models.ImageField(upload_to='events/', verbose_name="Фото",null=True)
    slug=models.SlugField(verbose_name="Символьный код", blank=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(unidecode(self.title))
        super().save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
        ordering = ['date']
