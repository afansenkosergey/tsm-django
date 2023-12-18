from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'pub_date', 'is_published')
    list_display_links = ('id', 'title')
    list_filter = ('title', 'pub_date', 'is_published')
    list_editable = ('is_published',)

admin.site.register(Article, ArticleAdmin)

