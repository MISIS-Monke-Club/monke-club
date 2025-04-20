from django.db import migrations
import random
from faker import Faker
from slugify import slugify
from django.utils.text import slugify as django_slugify

def create_vacancy_mock_data(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Vacancy = apps.get_model('vacancies', 'Vacancy')
    Stack = apps.get_model('vacancies', 'Stack')
    WorkType = apps.get_model('vacancies', 'WorkType')

    fake = Faker("ru_RU")

    # Создание стеков и типов работы
    stacks_titles = ['Python', 'Django', 'React', 'Docker', 'PostgreSQL']
    work_types_titles = ['Удаленная', 'Офис', 'Гибрид']

    stack_objs = []
    for title in stacks_titles:
        obj, _ = Stack.objects.get_or_create(title=title)
        stack_objs.append(obj)

    work_type_objs = []
    for title in work_types_titles:
        obj, _ = WorkType.objects.get_or_create(title=title)
        work_type_objs.append(obj)

    users = list(User.objects.all())
    used_slugs = set()

    for _ in range(30):
        title = fake.job()
        slug_base = slugify(title)
        slug = slug_base
        counter = 1
        while slug in used_slugs or Vacancy.objects.filter(slug=slug).exists():
            slug = f"{slug_base}-{counter}"
            counter += 1
        used_slugs.add(slug)

        vacancy = Vacancy.objects.create(
            user=random.choice(users) if users else None,
            title=title,
            slug=slug,
            description=fake.text(max_nb_chars=400),
            data_end=fake.date_between(start_date="+10d", end_date="+90d"),
            price=random.choice([None, random.randint(50000, 200000)]),
            work_type=random.choice(work_type_objs),
            job_experience=random.randint(0, 10),
            schedule=random.choice(["Полный день", "Гибкий график", "Удалёнка"]),
            work_space=random.choice(["Москва", "Удалённо", "Санкт-Петербург", "Казань"])
        )

        # Назначить случайные стеки
        random_stacks = random.sample(stack_objs, k=random.randint(1, len(stack_objs)))
        vacancy.stack.set(random_stacks)

class Migration(migrations.Migration):

    dependencies = [
        ('user','0004_create_mock_user'),
        ('vacancies', '0005_vacancy_user'), 
    ]

    operations = [
        migrations.RunPython(create_vacancy_mock_data),
    ]