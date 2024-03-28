FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR look_near_car/

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .