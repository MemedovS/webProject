from django.core.management.base import BaseCommand
from ...models import Order

class Command(BaseCommand):
    help = "List all orders."

    def handle(self, *args, **kwargs):
        orders = Order.objects.all()
        if orders.exists():
            for order in orders:
                self.stdout.write(f'Order ID: {order.id}, Client: {order.client.name}, Total: {order.total_amount}, Date: {order.order_date}')
                self.stdout.write('Products:')
                for product in order.products.all():
                    self.stdout.write(f' - {product.name} (${product.price})')
                self.stdout.write('---')
        else:
            self.stdout.write(self.style.ERROR('No orders found'))
