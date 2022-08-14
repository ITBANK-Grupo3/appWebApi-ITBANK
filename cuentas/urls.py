from django.urls import path
from . import views

urlpatterns = [
    path("", views.paquetes, name="paquetes"),
]
