FROM python:3.12
WORKDIR .
COPY requirements.txt .

RUN apt-get update && apt-get -y install cron nano

COPY crontab /etc/cron.d/crontab
RUN chmod 0644 /etc/cron.d/crontab
RUN crontab /etc/cron.d/crontab

RUN pip install -r requirements.txt
COPY . .

CMD ["sh", "-c", "python manage.py migrate"]