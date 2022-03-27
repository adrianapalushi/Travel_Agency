from django.contrib import admin

from .models import Continent, Country, City, Hotel, Airport, Trip

admin.site.register(Continent)

admin.site.register(Country)

admin.site.register(City)



@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ["name", "standard"]

class TripAdmin(admin.ModelAdmin):
    list_display = ["from_city", "to_city", "date_of_departure"]



admin.site.register(Airport)
admin.site.register(Trip)