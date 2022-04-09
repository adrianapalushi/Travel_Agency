from django.urls import path

from trips import views


urlpatterns = [
    path("", views.get_trip_list, name="trip_list"),
    path("<int:pk>/", views.get_trip_details, name="trip_details"),
]
