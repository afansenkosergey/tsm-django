from django.shortcuts import render
from django.views import View
from .models import Product, Category


class HomePageView(View):
    def get(self, request):
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'shop/home.html',  context=context)


class CategoryPageView(View):
    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        products = Product.objects.filter(category=category)
        context = {
            'category': category,
            'products': products
        }
        return render(request, 'shop/category.html', context=context)


class ProductPageView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        context = {
            'product': product
        }
        return render(request, 'shop/product.html', context=context)
