import json
import os

from django.core.management.base import BaseCommand
from django.conf import settings

from control_panel.models import Master


class Command(BaseCommand):
    def handle(self, *args, **options):
        filename = 'masters.json'
        masters_path = os.path.join(settings.BASE_DIR, f'fixtures/{filename}')
        with open(masters_path, 'r') as file:
            masters = json.load(file)['masters']
        new_masters = [Master(name=x) for x in masters]
        Master.objects.bulk_create(new_masters)
