from django import forms

from .models import *


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text']


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
