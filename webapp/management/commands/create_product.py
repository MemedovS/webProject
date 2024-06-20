from django.core.management.base import BaseCommand
from ...models import Product


class Command(BaseCommand):
    help = "Create a new product."

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Product name')
        parser.add_argument('description', type=str, help='Product description')
        parser.add_argument('price', type=float, help='Product price')
        parser.add_argument('quantity', type=int, help='Product quantity')

    def handle(self, *args, **kwargs):
        name = kwargs.get('name')
        description = kwargs.get('description')
        price = kwargs.get('price')
        quantity = kwargs.get('quantity')

        product = Product(name=name, description=description, price=price, quantity=quantity)
        product.save()

        self.stdout.write(self.style.SUCCESS(f'Product {name} created successfully'))


