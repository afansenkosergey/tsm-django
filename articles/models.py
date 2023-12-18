from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Список статей'
        verbose_name_plural = 'Список статей'
        ordering = ['-pub_date']
