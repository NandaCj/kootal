FROM python:3.6.9

WORKDIR kootal_app

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN apt update && apt install -y g++ build-essential libpq-dev

COPY kootal/kootal kootal_app

RUN cd kootal_app

EXPOSE 8000

ENTRYPOINT ["python", "manage.py", "runserver"]