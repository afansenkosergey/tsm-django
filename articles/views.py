from django.shortcuts import render

from .models import Article


def article_list(request):
    articles = Article.objects.all()
    context = {
        'title': 'Список статей',
        'articles': articles
    }
    return render(request, 'articles/article_list.html', context=context)