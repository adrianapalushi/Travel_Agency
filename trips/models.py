from django.db import models

class Continent(models.Model):
    name = models.CharField(max_length=30)

class Country(models.Model):
    name = models.CharField(max_length=50)
    continent = models.ForeignKey(Continent, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "country"
        verbose_name_plural = "countries"
    


class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "city"
        verbose_name_plural = "cities"
    
