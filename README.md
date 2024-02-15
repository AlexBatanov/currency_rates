#  Ⓚ

### Это тестовое задание, которе позволяет отображать курсы валют по отношению к российскому рублю на определенную дату.
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

4. Для загрузки и автоматического обновления курсов валют запустите cron:
```
sudo docker-compose exec -it backend service cron start
```

5. По умолчанию курсы валют обновляются раз в сутки. Чтобы изменить частоту обновления, отредактируйте файл **crontab** в директории **currency_rates_project**.
Информация для установки временого интервала https://help.ubuntu.com/community/CronHowto#Crontab_Lines

### Локальный Запуск

1. Установите зависимости:
```
pip install -r requirements.txt
```

2. Примените миграции:
```
python manage.py migrate
```

3. Создайте суперпользователя:
```
python manage.py createsuperuser
```

4. Загрузите и обновите курсы валют:
```
python manage.py update_currency_rates
```

5. Для постоянного обновления курсов валют потребуется запустить cron:
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


### Доступ к Проекту

Проект будет доступен по адресу http://localhost:8000/rate/
