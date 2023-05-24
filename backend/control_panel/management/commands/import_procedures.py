import json
import os

from django.core.management.base import BaseCommand
from django.conf import settings

from control_panel.models import Procedure


class Command(BaseCommand):
    def handle(self, *args, **options):
        filename = 'procedures.json'
        procedures_path = os.path.join(settings.BASE_DIR, f'static/{filename}')
        with open(procedures_path, 'r') as file:
            procedures = json.load(file)['procedures']
        new_procedures = [Procedure(title=x) for x in procedures]
        Procedure.objects.bulk_create(new_procedures)