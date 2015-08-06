# PrintSpeeder

## Розгортання

Для розгортання проекту локально, виконайте наступні команди:

1. Клонуйте репозитарій `git clone https://github.com/Q-bart/PrintSpeeder.git`
2. Встановіть python (якщо ще не встановлено)
3. Встановіть залежності `pip install -r requirements.txt`
4. В 'PrintSpeeder\PrintSpeeder' створіть файл `local_settings.py`. Для прикладу:

```
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'name_db',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

```

Далі: 

1. Створіть структуру базу даних `python manage.py migrate` - запустити в корені проекту(тільки 1 раз). 
2. Для запуску локально виконати `python manage.py runserver`
