from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView
from .forms import *
from .models import Article, Author


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'


def author_detail(request, author_id: int):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'articles/author_detail.html', {'author': author})


def authors_page(request):
    authors = Author.objects.all()
    return render(request, 'articles/authors_page.html', {'authors': authors})


def like(request, article_id: int):
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
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        author_form = AuthorForm(request.POST)
        if article_form.is_valid() and author_form.is_valid():
            author = author_form.save()
            article = article_form.save(commit=False)
            article.author = author
            article.save()
            return redirect('articles:list')
    else:
        article_form = ArticleForm()
        author_form = AuthorForm()

    return render(request, 'articles/add_article.html', {'article_form': article_form, 'author_form': author_form})


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comment = Comment.objects.filter(article=article)
    return render(request, 'articles/article_detail.html', {'article': article, 'comments': comment})


def add_comment(request, article_id):
    if request.method == 'POST':
        article = get_object_or_404(Article, id=article_id)
        user = request.user
        text = request.POST['comment_text']

        Comment.objects.create(article=article, user=user, text=text)

    return redirect('articles:detail', article_id=article_id)


# Registration and authentication

def register_page(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('articles:login')
        else:
            messages.error(request, 'Form is invalid!')
    context = {'form': form}
    return render(request, 'registration/register.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('articles:list')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'registration/login.html')


def logout_page(request):
    logout(request)
    return redirect('articles:list')
