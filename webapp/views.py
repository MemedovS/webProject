# views.py
from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from .models import Client, Order, Product
from .form import ProductForm


def client_detail(request, client_id):
    client = Client.objects.get(pk=client_id)
    orders = Order.objects.filter(client=client)
    return render(request, 'webapp/client_detail.html', {'client': client, 'orders': orders})


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'webapp/client_list.html', {'clients': clients})


def client_orders(request, client_id):
    # Получаем клиента по переданному client_id
    client = Client.objects.get(pk=client_id)

    # Текущая дата и время
    now = timezone.now()

    # Время неделю назад от текущего времени
    week_ago = now - timedelta(days=7)

    # Время месяц назад от текущего времени
    month_ago = now - timedelta(days=30)

    # Время год назад от текущего времени
    year_ago = now - timedelta(days=365)

    # Находим заказы клиента, сделанные за последнюю неделю
    orders_week = Order.objects.filter(client=client, order_date__gte=week_ago)

    # Находим заказы клиента, сделанные за последний месяц
    orders_month = Order.objects.filter(client=client, order_date__gte=month_ago)

    # Находим заказы клиента, сделанные за последний год
    orders_year = Order.objects.filter(client=client, order_date__gte=year_ago)

    # Получаем уникальные продукты, заказанные за последнюю неделю
    products_week = {product for order in orders_week for product in order.products.all()}

    # Получаем уникальные продукты, заказанные за последний месяц
    products_month = {product for order in orders_month for product in order.products.all()}

    # Получаем уникальные продукты, заказанные за последний год
    products_year = {product for order in orders_year for product in order.products.all()}

    # Формируем контекст для передачи в шаблон
    context = {
        'client': client,  # Клиент
        'products_week': products_week,  # Продукты за неделю
        'products_month': products_month,  # Продукты за месяц
        'products_year': products_year,  # Продукты за год
    }

    # Отображаем шаблон client_orders.html с переданным контекстом
    return render(request, 'webapp/client_orders.html', context)


def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Перенаправление на список продуктов или другую страницу
    else:
        form = ProductForm()
    return render(request, 'webapp/add_product.html', {'form': form})


def product_list(request):
    products = Product.objects.all()
    return render(request, 'webapp/product_list.html', {'products': products})


###

from django.db.models import Sum


def total_in_db(request):
    total = Product.objects.aggregate(Sum('quantity'))
    context = {
        'title': 'Общее количество посчитано в базе данных',
        'total': total,
    }
    return render(request, 'webapp/total_count.html', context)
