from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path(
        'reservar/<int:consola_id>/',
        views.reservar,
        name='reservar'
    ),
]