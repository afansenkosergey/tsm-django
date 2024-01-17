from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect

from .models import Product, Category, Order, OrderEntry, Profile


def category_detail(request, pk):
    """
        Отображает подробную информацию о конкретной категории и ее продуктах.
    """

    categories = Category.objects.all()
    category = Category.objects.get(pk=pk)
    products = Product.objects.filter(category=category)
    return render(request, 'shop/category.html',
                  {'category': category, 'products': products, 'categories': categories})


def product_page(request, pk):
    """
    Отображает подробную информацию о конкретном продукте.
    """
    product = Product.objects.get(pk=pk)
    categories = Category.objects.all()
    return render(request, 'shop/product.html', {'product': product, 'categories': categories})


def category_list(request):
    """
     Отображает список всех категорий.
    """
    categories = Category.objects.all()
    paginator = Paginator(categories, 4)
    page = request.GET.get('page')
    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)
    return render(request, 'shop/category_list.html', {'categories': categories})


@login_required
def add_to_cart(request, product_id):
    """
        Добавляет продукт в корзину пользователя.
    """
    product = get_object_or_404(Product, id=product_id)
    profile = Profile.objects.get(user=request.user)
    if not profile.shopping_cart:
        order = Order.objects.create(profile=profile)
        profile.shopping_cart = order
        profile.save()
    else:
        order = profile.shopping_cart
    order_entry, created = OrderEntry.objects.get_or_create(order=order, product=product)
    if not created:
        order_entry.count += 1
        order_entry.save()

    return redirect('shop:product', pk=product_id)


@login_required
def my_cart(request):
    """
        Отображает корзину пользователя с перечнем добавленных продуктов.
    """
    categories = Category.objects.all()
    profile = Profile.objects.get(user=request.user)
    order = Order.objects.filter(profile=profile, status=Order.Status.INITIAL).first()
    if not order:
        order = Order.objects.create(profile=profile, status=Order.Status.INITIAL)
    total_amount = sum(entry.count * entry.product.price for entry in order.entries.all())
    return render(request, 'shop/my_cart.html',
                  {'order': order, 'total_amount': total_amount, 'categories': categories})


@login_required
def update_quantity(request):
    """
        Обновляет количество продукта в корзине пользователя.
    """
    entry_id = request.POST.get('entry_id')
    quantity = request.POST.get('quantity')
    entry = OrderEntry.objects.get(id=entry_id)
    entry.count = quantity
    entry.save()
    return redirect('shop:my_cart')


@login_required
def remove_entry(request):
    """
        Удаляет запись о продукте из корзины пользователя.
    """
    entry_id = request.POST.get('entry_id')
    entry = OrderEntry.objects.get(id=entry_id)
    entry.delete()
    return redirect('shop:my_cart')


@login_required
def clear_cart(request):
    """
        Очищает все продукты из корзины пользователя.
    """
    OrderEntry.objects.all().delete()
    return redirect('shop:my_cart')


@login_required
def process_order(request):
    """
    Обрабатывает заказ пользователя, создавая новый заказ с продуктами из корзины покупок.
    """
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        order = Order.objects.create(profile=profile, status=Order.Status.COMPLETED)
        if profile.shopping_cart.entries.exists():
            entries = profile.shopping_cart.entries.all()
            for entry in entries:
                order.entries.create(product=entry.product, count=entry.count)
            profile.shopping_cart.entries.all().delete()
            return render(request, 'shop/order_success.html', {'order': order})

    return redirect('shop:my_cart')


@login_required
def user_profile(request):
    """
        Отображает информацию о профиле пользователя и последние заказы.
    """
    categories = Category.objects.all()
    user = request.user
    orders = Order.objects.filter(profile=user.profile).order_by('-id')[:5]
    for order in orders:
        entries = order.entries.all()
        total_quantity = sum(entry.count for entry in entries)
        order.total_quantity = total_quantity

        total_amount = sum(entry.product.price * entry.count for entry in entries)
        order.total_amount = total_amount
        order.save()

    return render(request, 'shop/user_profile.html',
                  {'user': user, 'orders': orders, 'categories': categories})


@login_required
def order_history(request):
    """
        Отображает историю заказов пользователя с пагинацией.
    """
    categories = Category.objects.all()
    orders = Order.objects.filter(profile=request.user.profile).order_by('-id')
    paginator = Paginator(orders.all(), 7)
    page = request.GET.get('page')
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)
    for order in orders:
        entries = order.entries.all()
        order.total_quantity = sum(entry.count for entry in entries)
        order.total_amount = sum(entry.product.price * entry.count for entry in entries)

    return render(request, 'shop/order_history.html', {'orders': orders, 'categories': categories})


@login_required
def repeat_order(request, order_id):
    """
        Обрабатывает заказ пользователя, создавая новый заказ с продуктами из корзины покупок.
    """
    order = get_object_or_404(Order, id=order_id, profile=request.user.profile)
    OrderEntry.objects.filter(order=request.user.profile.shopping_cart).delete()
    for entry in order.entries.all():
        OrderEntry.objects.create(order=request.user.profile.shopping_cart, product=entry.product, count=entry.count)

    return redirect('shop:my_cart')
