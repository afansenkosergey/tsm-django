import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()

from polls.models import Question, Choice



with open('polls_data.json', 'r') as file:
    data = json.load(file)

for question_text, choices_data in data.items():
    question = Question.objects.create(question_text=question_text)

    for choice_text, votes in choices_data.items():
        Choice.objects.create(question=question, choice_text=choice_text, votes=votes)

print('Объекты успешно созданы.')