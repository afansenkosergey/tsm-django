from django.contrib import admin

from .models import Category, Product, OrderEntry, Order
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profile"


class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'shopping_cart']


class ProductInline(admin.StackedInline):
    model = Product
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ProductInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price']
    list_filter = ['category']
    search_fields = ['name']
    list_per_page = 10


@admin.register(OrderEntry)
class OrderEntryAdmin(admin.ModelAdmin):
    list_display = ['product', 'count', 'order']


class OrderEntryInline(admin.TabularInline):
    model = OrderEntry


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['profile', 'status']
    inlines = [OrderEntryInline]
