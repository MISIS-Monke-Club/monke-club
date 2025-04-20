from django.db import migrations
import random
from datetime import timedelta
from django.utils import timezone
from faker import Faker
from django.utils.text import slugify
from unidecode import unidecode

def create_mock_data(apps, schema_editor):
    Event = apps.get_model('events', 'Event')
    EventType = apps.get_model('events', 'EventType')

    fake = Faker("ru_RU")

    types = [
        "Концерт",
        "Выставка",
        "Мастер-класс",
        "Лекция",
        "Фестиваль",
        "Спектакль",
        "Кино"
    ]

    event_type_objs = []
    for t in types:
        obj, _ = EventType.objects.get_or_create(type_name=t)
        event_type_objs.append(obj)

    used_slugs = set()

    for _ in range(50):
        title = fake.unique.sentence(nb_words=4)
        slug_base = slugify(unidecode(title))
        slug = slug_base
        counter = 1
        while slug in used_slugs or Event.objects.filter(slug=slug).exists():
            slug = f"{slug_base}-{counter}"
            counter += 1
        used_slugs.add(slug)

        date = timezone.now() + timedelta(days=random.randint(-30, 60), hours=random.randint(0, 23))
        price = random.choice([None, 0, random.randint(100, 5000)])
        location = fake.city()
        description = fake.paragraph(nb_sentences=5)
        registration_link = fake.url() if random.random() > 0.3 else None
        event_type = random.choice(event_type_objs)

        Event.objects.create(
            title=title,
            slug=slug,
            date=date,
            price=price,
            location=location,
            description=description,
            registration_link=registration_link,
            event_type=event_type
        )

class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_merge_0002_alter_event_image_mock_data'),  # замените при необходимости
    ]

    operations = [
        migrations.RunPython(create_mock_data),
    ]