from django.shortcuts import render

from trips.models import Trip


def home(request):
    promoted_trips = (Trip
        .objects
        .prefetch_related('photos')
        .filter(promoted=True)
        .order_by('date_of_departure')[:3]
    )
    return render(request, "pages/home.html", {
        "promoted_trips": promoted_trips
    })


def about(request):
   
    return render(request, "pages/about.html",)
