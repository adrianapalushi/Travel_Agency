import io
import random
import datetime as dt

from django.core.files.images import ImageFile
from django.core.management.base import BaseCommand, CommandError
from faker import Faker

from trips.models import Photo, Trip, City


class Command(BaseCommand):
    def handle(self, *args, **options):
        faker = Faker()

        cities = [city for city 
            in City.objects.prefetch_related('hotel_set', 'airport_set').all()
        ]

        for i in range(10):
            from_city = random.choice(cities)
            to_city = random.choice(cities)

            trip = Trip()

            trip.from_city = from_city
            trip.from_airport = from_city.airport_set.first()

            trip.to_city = to_city
            trip.to_airport = to_city.airport_set.first()
            trip.to_hotel = random.choice([h for h in to_city.hotel_set.all()])

            trip.date_of_departure = faker.date_this_year(after_today=True)
            trip.number_of_days = random.randrange(2, 15)
            trip.date_of_return = trip.date_of_departure + dt.timedelta(days=trip.number_of_days)
            trip.trip_type = random.choice([typ[0] for typ in Trip.TYPES])

            trip.price_for_adult = faker.pyfloat(left_digits=4, right_digits=0, positive=True, min_value=100, max_value=2500)
            trip.price_for_child = faker.pyfloat(left_digits=4, right_digits=0, positive=True, min_value=50, max_value=trip.price_for_adult)
            trip.number_of_adults = random.randrange(1, 13)
            trip.number_of_children = random.randrange(1, 9)

            trip.promoted = faker.pybool()
            trip.save()

            for i in range(random.randrange(1, 16)):
                photo = Photo(trip=trip, caption=faker.paragraph(), is_cover=i == 0)
                photo.photo = ImageFile(io.BytesIO(faker.image(size=(800, 600))), name=f"{faker.file_name(extension='png')}")
                photo.save()
