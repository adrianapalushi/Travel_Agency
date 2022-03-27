from django.db import models
from django.forms import CharField

class Continent(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "continent"
        verbose_name_plural = "continents"

    def __str__(self) -> str:
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=50)
    continent = models.ForeignKey(Continent, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "country"
        verbose_name_plural = "countries"
    
    def __str__(self) -> str:
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "city"
        verbose_name_plural = "cities"

    def __str__(self) -> str:
        return self.name


class Hotel(models.Model):
    name = models.CharField(max_length=40 , null=False)
    standard = models.IntegerField()
    description = models.TextField("description", null=False)
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "hotel"
        verbose_name_plural = "hotels"

    def __str__(self) -> str:
        return self.name

class Airport(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "airport"
        verbose_name_plural = "airports"

    def __str__(self) -> str:
        return self.name


class Trip(models.Model):
    BED_AND_BREAKFAST = 'BB'
    HALF_BOARD = 'HB'
    FULL_BOARD = 'FB'
    ALL_INCLUSIVE = 'AI'
    TYPES = [
        (BED_AND_BREAKFAST, 'Bed & Breakfast'),
        (HALF_BOARD, 'Half Board'),
        (FULL_BOARD, 'Full Board'),
        (ALL_INCLUSIVE, 'All Inclusive'),
    ]

    from_city = models.ForeignKey(City, null=True, on_delete=models.CASCADE, related_name="from_trips")
    from_airport = models.ForeignKey(Airport, null=True, on_delete=models.SET_NULL, related_name="from_trips")
    to_city = models.ForeignKey(City, null=True, on_delete=models.CASCADE, related_name="to_trips")
    to_hotel = models.ForeignKey(Hotel, null=True, on_delete=models.SET_NULL, related_name="to_trips")
    to_airport = models.ForeignKey(Airport, null=True, on_delete=models.SET_NULL, related_name="to_trips")
    date_of_departure = models.DateTimeField()
    date_of_return = models.DateTimeField()
    number_of_days = models.IntegerField()
    trip_type = models.CharField(max_length=2, choices=TYPES)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    price_for_adult = models.FloatField(null=True, default="not mentioned by owner",blank=True)
    price_for_child = models.FloatField(null=True, default="not mentioned by owner", blank=True)
    promoted = models.IntegerField(null=True, default="not mentioned by owner", blank=True,)
    nr_of_adult = models.IntegerField()
    nr_of_child = models.IntegerField()


