# create a command hello

from django.core.management.base import BaseCommand

# hello world

class Command(BaseCommand):
    help = 'Prints hello world'

    def handle(self, *args, **options):
        print('Hello world')

# next step is to run the command
# python manage.py hello 

#unknown command: hello

# to fix this we need to add the command to the installed apps in the settings.py file
