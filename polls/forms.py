from django import forms
from django.utils import timezone
from django.contrib.admin.widgets import AdminDateWidget


class QuestionForm(forms.Form):
    question_text = forms.CharField(label='Question Text', max_length=100)
    publication_date = forms.DateField(initial=timezone.now().date(),
                                       widget=forms.SelectDateWidget)
    choices = forms.ChoiceField(label='Choices', widget=forms.Textarea)



