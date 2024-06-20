from django.core.management.base import BaseCommand
from ...models import Order, Product

class Command(BaseCommand):
    help = "Update order by id."

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int, help='Order ID')
        parser.add_argument('--add_products', type=int, nargs='+', help='Product IDs to add', default=None)
        parser.add_argument('--remove_products', type=int, nargs='+', help='Product IDs to remove', default=None)

    def handle(self, *args, **kwargs):
        order_id = kwargs.get('order_id')
        order = Order.objects.filter(pk=order_id).first()

        if order is not None:
            if kwargs.get('add_products'):
                for product_id in kwargs['add_products']:
                    try:
                        product = Product.objects.get(pk=product_id)
                        order.products.add(product)
                    except Product.DoesNotExist:
                        self.stdout.write(self.style.ERROR(f'Product with ID {product_id} does not exist.'))

            if kwargs.get('remove_products'):
                for product_id in kwargs['remove_products']:
                    try:
                        product = Product.objects.get(pk=product_id)
                        order.products.remove(product)
                    except Product.DoesNotExist:
                        self.stdout.write(self.style.ERROR(f'Product with ID {product_id} does not exist.'))

            order.calculate_total()
            self.stdout.write(self.style.SUCCESS(f'Order {order_id} updated successfully'))
        else:
            self.stdout.write(self.style.ERROR(f'Order {order_id} not found'))
