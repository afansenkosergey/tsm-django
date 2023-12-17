import json
from polls.models import Question, Choice


def populate_polls_database(json_file_path, clean_database=True):
    if clean_database:
        Question.objects.all().delete()
        Choice.objects.all().delete()

    with open(json_file_path, 'r') as file:
        data = json.load(file)

    for question_text, choices_data in data.items():
        question = Question.objects.create(question_text=question_text)

        for choice_text, votes in choices_data.items():
            Choice.objects.create(question=question, choice_text=choice_text, votes=votes)
