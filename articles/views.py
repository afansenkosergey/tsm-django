from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from .forms import *
from .models import Article, Author


class ArticleListView(ListView):
    """
    Представление для отображения списка статей.

    Attributes:
        model (Article): Модель, используемая для получения данных.
        template_name (str): Имя шаблона, используемого для отображения списка статей.
        context_object_name (str): Имя переменной контекста, содержащей объекты статей.

    """
    model = Article
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'


def author_detail(request, author_id: int):
    """
    Представление для отображения подробной информации об авторе.

    Args:
        request (HttpRequest): Запрос от клиента.
        author_id (int): Идентификатор автора.

    Returns:
        HttpResponse: Ответ с отображением страницы с информацией об авторе.

    """
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'articles/author_detail.html', {'author': author})


def authors_page(request):
    """
    Представление для отображения страницы с информацией об авторах, пользователях и статьях.

    Args:
        request (HttpRequest): Запрос от клиента.

    Returns:
        HttpResponse: Ответ с отображением страницы с информацией об авторах, пользователях и статьях.

    """
    authors = Author.objects.all()
    users = User.objects.all()
    articles = Article.objects.all()

    return render(request, 'articles/authors_page.html',
                  {'authors': authors, 'users': users, 'articles': articles, 'user': request.user})


def user_detail(request, username: str):
    """
    Представление для отображения информации о пользователе и его статьях.

    Args:
        request (HttpRequest): Запрос от клиента.
        username (str): Имя пользователя.

    Returns:
        HttpResponse: Ответ с отображением страницы с информацией о пользователе и его статьях.

    """
    user = get_object_or_404(User, username=username)
    articles = Article.objects.filter(user=user)
    return render(request, 'articles/user_detail.html', {'user': user, 'articles': articles})


def like(request, article_id: int):
    """
    Вьюха для обработки лайков для статей.

    Args:
        request (HttpRequest): Запрос от клиента.
        article_id (int): Идентификатор статьи.

    Returns:
        HttpResponse: Перенаправление на страницу деталей статьи.

    """
    article = get_object_or_404(Article, id=article_id)
    liked_articles = request.session.get('liked_articles', [])
    if article_id in liked_articles:
        article.likes -= 1
        liked_articles.remove(article_id)
    else:
        article.likes += 1
        liked_articles.append(article_id)
    article.save()
    request.session['liked_articles'] = liked_articles
    return redirect('articles:detail', article_id)


@login_required(login_url='articles:login')
def add_article(request):
    """
    Вьюха для добавления новой статьи.

    Args:
        request (HttpRequest): Запрос от клиента.

    Returns:
        HttpResponse: Ответ с отображением формы добавления статьи или перенаправление на список статей.

    """
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:list')
    else:
        article_form = ArticleForm()

    return render(request, 'articles/add_article.html', {'article_form': article_form})


def article_detail(request, article_id: int):
    """
    Представление для отображения подробной информации о статье и ее комментариях.

    Args:
        request (HttpRequest): Запрос от клиента.
        article_id (int): Идентификатор статьи.

    Returns:
        HttpResponse: Ответ с отображением страницы с информацией о статье и комментариях.

    """
    article = get_object_or_404(Article, id=article_id)
    comment = Comment.objects.filter(article=article)
    return render(request, 'articles/article_detail.html',
                  {'article': article, 'comments': comment, 'user': request.user})


def add_comment(request, article_id: int):
    """
    Вьюха для добавления комментария к статье.

    Args:
        request (HttpRequest): Запрос от клиента.
        article_id (int): Идентификатор статьи.

    Returns:
        HttpResponse: Перенаправление на страницу деталей статьи.

    """
    if request.method == 'POST':
        article = get_object_or_404(Article, id=article_id)
        user = request.user
        text = request.POST['comment_text']

        Comment.objects.create(article=article, user=user, text=text)

    return redirect('articles:detail', article_id=article_id)

