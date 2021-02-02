from django.urls import path

from . import views

urlpatterns = [
    path("tables/", views.weather_info, name="weather_data"),
    path("search/", views.search, name="weather_search"),
    path("", views.main, name="main"),
]