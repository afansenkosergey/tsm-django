from django.shortcuts import render
from django.views import View
from .models import Product, Category


class HomePageView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'shop/home.html', {'categories': categories})


class CategoryPageView(View):
    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        products = Product.objects.filter(category=category)
        return render(request, 'shop/category.html', {'category': category, 'products': products})


class ProductPageView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'shop/product.html', {'product': product})


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'shop/category_list.html', {'categories': categories})
