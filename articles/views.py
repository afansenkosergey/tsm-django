from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, ListView
from .forms import *
from .models import Article, Author


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'


def detail(request, article_id: int):
    article = get_object_or_404(Article, id=article_id)
    context = {
        'article': article
    }
    return render(request, 'articles/article_detail.html', context=context)


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'articles/author_detail.html', {'author': author})

def authors_page(request):
    authors = Author.objects.all()
    return render(request, 'articles/authors_page.html', {'authors': authors})


def like(request, article_id: int):
    article = get_object_or_404(Article, id=article_id)
    article.likes += 1
    article.save()
    return redirect('articles:detail', article_id)


@login_required
def add_article(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        author_form = AuthorForm(request.POST)
        if article_form.is_valid() and author_form.is_valid():
            author = author_form.save()  # Сначала сохраните автора
            article = article_form.save(commit=False)
            article.author = author
            article.save()
            return redirect('articles:list')
    else:
        article_form = ArticleForm()
        author_form = AuthorForm()

    return render(request, 'articles/add_article.html', {'article_form': article_form, 'author_form': author_form})

