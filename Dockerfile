FROM python:3.9

WORKDIR /app/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app/requirements.txt

EXPOSE 8000

RUN pip install --upgrade pip setuptools wheel
RUN pip install -r ./requirements.txt

COPY . /app

CMD ["uvicorn", "app.app:app", "--reload", "--workers", "1", "--host", "0.0.0.0", "--port", "8000"]
