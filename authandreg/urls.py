from django.urls import path
from . import views

app_name = 'authandreg'
urlpatterns = [
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('update_profile/', views.update_profile, name='update_profile'),
]
