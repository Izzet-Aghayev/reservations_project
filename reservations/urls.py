from django.urls import path

from reservations import views as reservation_views



urlpatterns = [
    path('', reservation_views.HomeView.as_view(), name='home'),
    path('resev/', reservation_views.CreateReservationView.as_view(), name='resev'),
]
