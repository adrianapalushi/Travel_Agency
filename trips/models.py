from django.db import models

class Continent(models.Model):
    name = models.CharField(max_length=30)

class Country(models.Model):
    name = models.CharField(max_length=50)
    
