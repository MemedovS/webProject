from django.core.management.base import BaseCommand
from ...models import Product

class Command(BaseCommand):
    help = "Display all products"

    def handle(self, *args, **kwargs):
        products = Product.objects.all()
        for product in products:
            self.stdout.write(f"Name: {product.name}, Description: {product.description}, Price: {product.price}, Quantity: {product.quantity}")
