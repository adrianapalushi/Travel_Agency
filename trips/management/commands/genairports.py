import random

from django.core.management.base import BaseCommand, CommandError

from trips.models import Airport, City


class Command(BaseCommand):
    def handle(self, *args, **options):
        for city in City.objects.all():
                ap = Airport(city=city, name=f'{city.name} International Airport')
                ap.save()
