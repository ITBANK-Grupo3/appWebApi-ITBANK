from django.urls import path
from . import views
from prestamos import views as prestamo_views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("", views.billetera, name="billetera"),
    path("tubanco/", views.tubanco, name="tubanco"),
    path("tubanco/compraventausd/", views.compraventausd, name="compraventausd"),
    path("graficos/", views.graficos, name="graficos"),
    path("prestamo/",prestamo_views.prestamo, name="prestamo")
]
