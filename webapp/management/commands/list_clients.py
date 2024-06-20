from django.core.management.base import BaseCommand
from ...models import Client

class Command(BaseCommand):
    help = "List all clients."

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        if clients.exists():
            for client in clients:
                self.stdout.write(f'ID: {client.id}, Name: {client.name}, Email: {client.email}, Phone Number: {client.phone_number}')
        else:
            self.stdout.write(self.style.ERROR('No clients found'))
