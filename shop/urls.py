from django.urls import path
from .views import HomePageView, CategoryPageView, ProductPageView

app_name = 'shop'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('category/<int:pk>', CategoryPageView.as_view(), name='category'),
    path('product/<int:pk>', ProductPageView.as_view(), name='product'),
]