from django.urls import path
from . import views
from .views import ArticleListView

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='list'),
    path('<int:article_id>', views.detail, name='detail'),
    path('<int:article_id>/like', views.like, name='like'),
    path('addarticle', views.add_article, name='add_article'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('authors/', views.authors_page, name='authors_page'),
]
