from django.core.management.base import BaseCommand
from ...models import Client

class Command(BaseCommand):
    help = "Update client by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client ID')
        parser.add_argument('--name', type=str, help='Client name', default=None)
        parser.add_argument('--email', type=str, help='Client email', default=None)
        parser.add_argument('--phone_number', type=str, help='Client phone number', default=None)
        parser.add_argument('--address', type=str, help='Client address', default=None)

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()

        if client is not None:
            updated_fields = []

            if kwargs.get('name'):
                client.name = kwargs['name']
                updated_fields.append('name')

            if kwargs.get('email'):
                client.email = kwargs['email']
                updated_fields.append('email')

            if kwargs.get('phone_number'):
                client.phone_number = kwargs['phone_number']
                updated_fields.append('phone_number')

            if kwargs.get('address'):
                client.address = kwargs['address']
                updated_fields.append('address')

            client.save(update_fields=updated_fields)
            self.stdout.write(self.style.SUCCESS(f'Client {pk} updated successfully'))
        else:
            self.stdout.write(self.style.ERROR(f'Client {pk} not found'))
