from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Article, Author, Comment


class ArticleForm(forms.ModelForm):
    """
    Форма для создания и редактирования объектов модели Article.

    Meta:
        model (Article): Модель, связанная с формой.
        fields (list): Список полей, которые будут отображены в форме.

    """

    class Meta:
        model = Article
        fields = ['title', 'text']


class AuthorForm(forms.ModelForm):
    """
    Форма для создания и редактирования объектов модели Author.

    Meta:
        model (Author): Модель, связанная с формой.
        fields (list): Список полей, которые будут отображены в форме.

    """

    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth']


class CommentForm(forms.ModelForm):
    """
    Форма для создания и редактирования объектов модели Comment.

    Meta:
        model (Comment): Модель, связанная с формой.
        fields (list): Список полей, которые будут отображены в форме.

    """

    class Meta:
        model = Comment
        fields = ['text']


class RegistrationForm(UserCreationForm):
    """
    Форма для регистрации новых пользователей.

    Attributes:
        first_name (CharField): Поле для ввода имени пользователя (необязательное).
        last_name (CharField): Поле для ввода фамилии пользователя (необязательное).
        email (EmailField): Поле для ввода адреса электронной почты пользователя.

    Meta:
        model (User): Модель, связанная с формой.
        fields (list): Список полей, которые будут отображены в форме регистрации.

    """
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
