from django.shortcuts import render

from .models import Trip


def get_trip_list(request):
    trips = Trip.objects.all()
    return render(request, 'trips/trip_list.html', context={
        'trips': trips
    })
