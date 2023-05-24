import json
import os

from django.core.management.base import BaseCommand
from django.conf import settings

from control_panel.models import Client


class Command(BaseCommand):
    def handle(self, *args, **options):
        filename = 'clients.json'
        clients_path = os.path.join(settings.BASE_DIR, f'static/{filename}')
        with open(clients_path, 'r') as file:
            clients = json.load(file)['clients']
        new_clients = [Client(name=x) for x in clients]
        Client.objects.bulk_create(new_clients)
