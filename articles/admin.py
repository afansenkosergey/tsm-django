from django.contrib import admin

from polls.models import Question, Choice
from .models import Article, Author


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'likes', 'is_popular')
    search_fields = ('title', 'authors', 'text')
    readonly_fields = ('likes',)
    fieldsets = (
        ('Поля для заполнения:', {
            'fields': ('title', 'authors', 'likes'),
        }),
        ('Статья:', {
            'fields': ('text',),
        }),
    )

    def is_popular(self, obj):
        return obj.is_popular()

    is_popular.boolean = True
    is_popular.short_description = 'Popular'


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth')
    search_fields = ('first_name', 'last_name')
