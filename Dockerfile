FROM python:3.9

WORKDIR /app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/requirements.txt

EXPOSE 8000

RUN pip install --upgrade pip setuptools wheel
RUN pip install -r ./requirements.txt

COPY . /app
