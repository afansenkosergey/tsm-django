from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('api.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
    path('shop/', include('shop.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('authandreg/', include('authandreg.urls')),
]
