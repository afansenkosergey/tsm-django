from django.urls import path

from shop.views import *

app_name = 'shop'
urlpatterns = [
    path('', category_list, name='category_list'),
    path('category/<int:pk>', category_detail, name='category'),
    path('product/<int:pk>', product_page, name='product'),
    path('my_cart/', my_cart, name='my_cart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('my_cart/', my_cart, name='my_cart'),
    path('clear_cart/', clear_cart, name='clear_cart'),
    path('update_quantity/', update_quantity, name='update_quantity'),
    path('clear_cart/', clear_cart, name='clear_cart'),
    path('remove_entry/', remove_entry, name='remove_entry'),
    path('process_order/', process_order, name='process_order'),
    path('user_profile/', user_profile, name='user_profile'),
    path('order_history/', order_history, name='order_history'),
    path('my_cart/repeat_order/<int:order_id>/', repeat_order, name='repeat_order'),
]
