FROM python:3.6.9

WORKDIR kootal_app

RUN apt update && apt install -y g++ build-essential libpq-dev

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY kootal kootal_app

EXPOSE 8000

RUN python kootal_app/manage.py collectstatic --noinput

ENTRYPOINT ["python", "kootal_app/manage.py", "runserver", "0.0.0.0:8000"]