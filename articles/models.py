from django.contrib.auth.models import User, AbstractUser
from django.db import models


class Author(models.Model):
    """
    Модель представляющая сущность "Автор".

    Attributes:
        first_name (str): Фамилия автора.
        last_name (str): Имя автора.
        date_of_birth (Date, optional): Дата рождения автора.

    Meta:
        verbose_name (str): Название модели в единственном числе для отображения в админке.
        verbose_name_plural (str): Название модели во множественном числе для отображения в админке.
        ordering (list): Список полей для сортировки записей.

    Methods:
        __str__(): Возвращает строковое представление объекта в формате "Фамилия Имя".
    """
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
    """
    Модель представляющая сущность "Статья".

    Attributes:
        title (str): Заголовок статьи.
        authors (ManyToManyField): Связь с моделью Author для указания авторов статьи.
        text (str): Текст статьи.
        pub_date (DateTime): Дата публикации статьи.
        likes (int, optional): Количество лайков для статьи (по умолчанию 0).
        user (ForeignKey): Связь с моделью User для указания пользователя, создавшего статью.

    Methods:
        __str__(): Возвращает строковое представление объекта в виде заголовка статьи.
        is_popular(): Возвращает True, если статья популярна (больше 100 лайков).
        save(*args, **kwargs): Переопределенный метод сохранения объекта, преобразует заголовок в верхний регистр.

    Meta:
        verbose_name (str): Название модели в единственном числе для отображения в админке.
        verbose_name_plural (str): Название модели во множественном числе для отображения в админке.
        ordering (list): Список полей для сортировки записей.
    """
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    authors = models.ManyToManyField(Author)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    likes = models.IntegerField(default=0, verbose_name="Количество лайков")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def is_popular(self):
        return self.likes > 100

    class Meta:
        verbose_name = 'Список статей'
        verbose_name_plural = 'Список статей'
        ordering = ['text']


class Comment(models.Model):
    """
    Модель представляющая сущность "Комментарий".

    Attributes:
        article (ForeignKey): Связь с моделью Article для указания статьи, к которой относится комментарий.
        user (ForeignKey): Связь с моделью User для указания пользователя, оставившего комментарий.
        text (str): Текст комментария.
        created_at (DateTime): Дата и время создания комментария.
    """
    article = models.ForeignKey(Article, on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
