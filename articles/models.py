from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="Фамилия")
    last_name = models.CharField(max_length=100, verbose_name="Имя")
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Дата рождения")

    class Meta:
        verbose_name = 'Авторы'
        verbose_name_plural = 'Авторы'
        ordering = ['first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    authors = models.ManyToManyField(Author)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    likes = models.IntegerField(default=0, verbose_name="Количество лайков")

    def __str__(self):
        return self.title

    def is_popular(self):
        return self.likes > 100

    class Meta:
        verbose_name = 'Список статей'
        verbose_name_plural = 'Список статей'
        ordering = ['text']


# Registration and authentication

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
