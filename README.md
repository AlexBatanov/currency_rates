#  Ⓚ

### Это тестовое задание, которе позволяет отображать курсы валют по отношению к российскому рублю на определенную дату.

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Docker Badge](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff&style=for-the-badge)

## Запрос

GET /rate/

### Параметры запроса

- charcode (строка): Код валюты (например, AUD)
- date (строка): Дата в формате YYYY-MM-DD

### Пример запроса

```
http://localhost:8000/rate/?charcode=AUD&date=2024-01-01
```

## Ответ

В случае успешного запроса, приложение вернет данные в формате JSON:
```
json
{
  "charcode": "AUD",
  "date": "2024-01-01",
  "rate": 57.0627
}
```
Если нет данных - статус код 404:
```
{
    "detail": "Страница не найдена."
}
```

### Запуск проекта в Docker

1. Склонируйте репозиторий и перейдите в папку проекта:
```
git clone git@github.com:AlexBatanov/currency_rates.git
cd currency_rates
```

2. Соберите и запустите проект в Docker:
```
sudo docker-compose up --build
```

3. Создание администратора:
```
sudo docker-compose exec -it backend python manage.py createsuperuser
```
4. Для первоначальной загрузки валют:
```
sudo docker-compose exec -it backend python manage.py update_currency_rates
```

5. Для загрузки и автоматического обновления курсов валют запустите cron:
```
sudo docker-compose exec -it backend service cron start
```

5. По умолчанию курсы валют обновляются раз в сутки. Чтобы изменить частоту обновления, отредактируйте файл **crontab** в директории **currency_rates_project**.
Информация для установки временого интервала https://help.ubuntu.com/community/CronHowto#Crontab_Lines

### Локальный Запуск
1. Перейти в дирректорию проекта:
```
cd currency_rates
```

2. Установите зависимости:
```
pip install -r requirements.txt
```

3. Примените миграции:
```
python manage.py migrate
```

4. Создайте суперпользователя:
```
python manage.py createsuperuser
```

5. Загрузите и обновите курсы валют:
```
python manage.py update_currency_rates
```

6. Для постоянного обновления курсов валют потребуется запустить cron:
    - Получение команды для crontab:
    ```
    bash create_crontab_command.sh
    ```
    - В терминале получим: export DJANGO_SETTINGS_MODULE='currency_rates_project.settings'; /ваш путь до интерпретатора/python3  /путь до mange.py/manage.py update_currency_rates - **копируем команду полностью**
    - Открываем задания для cron:
    ```
    crontab -e
    ```
    - В открывшемся редакторе указываем интервал выполнения и вставляем скопированную команду. Информация для установки временого интервала https://help.ubuntu.com/community/CronHowto#Crontab_Lines
    - Сохраняем изменения и выйходим из редактора.
    - Теперь курс валют будет автоматически обновляться согласно настройкам.
7. Запуск проекта:
```
python manage.py runserver
```
Для остановки задачи cron - выполнить crontab -e, удалить команду и сохранить

### Доступ к Проекту

Проект будет доступен по адресу http://localhost:8000/rate/

### Автор
[Batanov Alexandr](https://github.com/AlexBatanov)
