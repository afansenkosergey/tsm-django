from django.urls import path
from . import views
from .views import ArticleListView

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='list'),
    path('<int:article_id>', views.article_detail, name='detail'),
    path('<int:article_id>/like', views.like, name='like'),
    path('addarticle', views.add_article, name='add_article'),
    path('article/<int:article_id>/add_comment/', views.add_comment, name='add_comment'),
    path('author/<int:author_id>/', views.author_detail, name='author_detail'),
    path('user/<str:username>/', views.user_detail, name='user_detail'),
    path('authors/', views.authors_page, name='authors_page'),
]
