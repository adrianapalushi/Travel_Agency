from django.contrib import admin

from .models import Continent, Country, City, Hotel, Airport

admin.site.register(Continent)

admin.site.register(Country)

admin.site.register(City)


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ["name", "standard"]


admin.site.register(Airport)
