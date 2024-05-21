from django.core.management.base import BaseCommand
from listings.models import Listing

class Command(BaseCommand):
    help = 'Prints the primary key values of YourModel'
    
    def handle(self, *args, **options):
        pks = Listing.objects.values_list('pk', flat=True)
        self.stdout.write("\n".join(map(str, pks)))
