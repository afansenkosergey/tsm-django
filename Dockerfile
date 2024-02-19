# Используем базовый образ Python
FROM python:3.11

# Установка переменной окружения для Python (может быть необязательно)
ENV PYTHONUNBUFFERED=1

# Создание и переход в рабочую директорию в контейнере
WORKDIR /app

# Копирование зависимостей проекта в контейнер
COPY requirements.txt /app/

# Установка зависимостей проекта
RUN pip install -r requirements.txt

# Копирование остальных файлов проекта в контейнер
COPY . /app/

# Открываем порт, на котором будет работать Django
EXPOSE 8000

RUN adduser --disabled-password app-user

USER app-user