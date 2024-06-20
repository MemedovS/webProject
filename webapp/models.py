from django.db import models
from decimal import Decimal


class Client(models.Model):
    name = models.CharField(max_length=100)  # Имя клиента
    email = models.EmailField(unique=True)  # Электронная почта клиента
    phone_number = models.CharField(max_length=15)  # Номер телефона клиента
    address = models.TextField()  # Адрес клиента
    registration_date = models.DateTimeField(auto_now_add=True)  # Дата регистрации клиента

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super(Client, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)  # Название товара
    description = models.TextField()  # Описание товара
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена товара
    quantity = models.PositiveIntegerField()  # Количество товара
    added_date = models.DateTimeField(auto_now_add=True)  # Дата добавления товара
    photo = models.ImageField(upload_to='product_photos/', blank=True, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders')  # Клиент, сделавший заказ
    products = models.ManyToManyField(Product, related_name='orders')  # Товары, входящие в заказ
    total_amount = models.DecimalField(max_digits=10, decimal_places=5)  # Общая сумма заказа
    order_date = models.DateTimeField(auto_now_add=True)  # Дата оформления заказа

    def __str__(self):
        return f"Order #{self.pk} by {self.client.name}"

    def calculate_total(self):
        total = Decimal(0)
        for product in self.products.all():
            total += product.price
        self.total_amount = total
