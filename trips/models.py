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
