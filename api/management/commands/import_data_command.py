from django.core.management.base import BaseCommand
from api.import_data import import_data

class Command(BaseCommand):
    help = 'Import data from CSV files to the database'
    def handle(self, *args, **options):
        import_data()
