pip install --no-cache-dir -r requirements.txt
echo "Создание новых миграций"
python manage.py makemigrations
echo "Применение миграций"
python manage.py migrate

echo "Creating superuser if none exists..."
python manage.py shell -c "
from django.contrib.auth import get_user_model
User = get_user_model()
username = 'root'
email = 'root@root.ru'
password = 'root'
if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f'Superuser \"{username}\" created successfully.')
else:
    print(f'Superuser \"{username}\" already exists.')
" && echo "Superuser creation completed."

python manage.py runserver 0.0.0.0:8000