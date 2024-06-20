from django.core.management.base import BaseCommand
from ...models import Client, Product, Order



class Command(BaseCommand):
    help = 'Create a new order.'

    def add_arguments(self, parser):
        parser.add_argument('client_id', type=int, help='Client ID')
        parser.add_argument('product_ids', nargs='+', type=int, help='Product IDs')

    def handle(self, *args, **kwargs):
        client_id = kwargs['client_id']
        product_ids = kwargs['product_ids']


        try:
            client = Client.objects.get(pk=client_id)
        except Client.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Client with ID {client_id} does not exist.'))
            return

        products = []
        total_amount = 0  # Инициализируем общую сумму заказа

        for product_id in product_ids:
            try:
                product = Product.objects.get(pk=product_id)
                products.append(product)
                total_amount += product.price  # Увеличиваем общую сумму на цену товара
            except Product.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Product with ID {product_id} does not exist.'))

        if not products:
            self.stdout.write(self.style.ERROR('No valid products provided.'))
            return

        # Создаем заказ
        order = Order.objects.create(client=client, total_amount=total_amount)

        # Устанавливаем товары для заказа
        order.products.set(products)

        self.stdout.write(self.style.SUCCESS(f'Order {order.id} created successfully.'))

