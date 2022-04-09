from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Trip


def get_trip_list(request):
    trips = Trip.objects.all()
    return render(request, 'trips/trip_list.html', context={
        'trips': trips
    })


def get_trip_details(request: HttpRequest, pk: int) -> HttpResponse:
    trip = (Trip
        .objects
        .select_related(
            "from_city", "from_airport",
            "to_city", "to_airport", "to_hotel"
        )
        .get(pk=pk)
    )
    # trip = get_object_or_404(Trip, pk=pk)
    return render(request, "trips/trip_details.html", context={
        "trip": trip
    })
