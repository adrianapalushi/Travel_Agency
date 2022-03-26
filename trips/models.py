from django.db import models

class Continent(models.Model):
    name = models.CharField(max_length=30)
