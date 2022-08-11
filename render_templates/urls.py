from urllib.parse import parse_qs
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("billetera/", views.billetera, name="billetera"),
]
