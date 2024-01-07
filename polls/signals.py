from django.db.models import signals
from polls.models import Question


def my_callback(sender, args, kwargs):
    print(f'Pre init. Sender: {sender}, args: {args}, kwargs: {kwargs}')


signals.post_save.connect(my_callback, sender=Question)