from django.contrib import admin
from .models import Client, Product, Order
from .admin_mixins import ExportAsCSVMixin


# Admin для модели Client
class ClientAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    list_display = ('name', 'email', 'phone_number', 'address', 'registration_date')  # Поля, отображаемые в списке
    search_fields = ('name', 'email', 'phone_number')  # Поля для поиска
    list_filter = ('registration_date',)  # Фильтры по дате регистрации
    actions = ['export_csv']


# Регистрация ClientAdmin с моделью Client
admin.site.register(Client, ClientAdmin)


# @admin.register(Product)-- можно так тоже регистривовать
# Admin для модели Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'added_date')  # Поля, отображаемые в списке
    search_fields = ('name',)  # Поля для поиска
    list_filter = ('added_date', 'price')  # Фильтры по дате добавления и цене
    readonly_fields = ('added_date',)  # Только для чтения: дата добавления

    # Метод для отображения цены в формате долларов
    def product_price(self, obj):
        return f"${obj.price}"


# Регистрация ProductAdmin с моделью Product
admin.site.register(Product, ProductAdmin)


# Admin для модели Order
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'total_amount', 'order_date')  # Поля, отображаемые в списке
    search_fields = ('client__name', 'client__email')  # Поля для поиска (доступ через связь с клиентом)
    list_filter = ('order_date', 'total_amount')  # Фильтры по дате заказа и общей сумме
    filter_horizontal = ('products',)  # Фильтр для множественного выбора продуктов
    readonly_fields = ('total_amount', 'order_date')  # Только для чтения: общая сумма и дата заказа


# Регистрация OrderAdmin с моделью Order
admin.site.register(Order, OrderAdmin)
