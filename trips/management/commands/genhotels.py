import random

from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from trips.models import Hotel, City


class Command(BaseCommand):
    def handle(self, *args, **options):
        faker = Faker()

        for city in City.objects.all():
            for i in range(random.randrange(2, 12)):
                hotel = Hotel(
                    name=f'{faker.city()} Hotel',
                    city=city,
                    standard=random.randint(1, 5),
                    description="\n\n".join(faker.paragraphs(3))
                )
                hotel.save()
