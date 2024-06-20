# seminar_2_app/management/commands/delete_client.py
from django.core.management.base import BaseCommand
from ...models import Client

class Command(BaseCommand):
    help = "Delete client by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        if client is not None:
            client.delete()
            self.stdout.write(self.style.SUCCESS(f'Client {pk} deleted successfully'))
        else:
            self.stdout.write(self.style.ERROR(f'Client {pk} not found'))