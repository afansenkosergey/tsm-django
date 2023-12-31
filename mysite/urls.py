from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('shop/', include('shop.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
