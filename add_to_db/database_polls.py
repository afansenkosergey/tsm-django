import json
import os
import sys

# Добавляем путь к каталогу проекта в sys.path
sys.path.append('/app')  # Замените '/app' на актуальный путь к вашему Django-проекту

# Настройка переменной окружения DJANGO_SETTINGS_MODULE
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

from polls.models import Question, Choice

with open('add_to_db/polls_data.json', 'r') as file:
    data = json.load(file)

for question_text, choices_data in data.items():
    question = Question.objects.create(question_text=question_text)

    for choice_text, votes in choices_data.items():
        Choice.objects.create(question=question, choice_text=choice_text, votes=votes)

print('Объекты успешно созданы.')
