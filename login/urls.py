from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login/login.html"), name="login"),
    path(
        "logout/", LogoutView.as_view(template_name="login/logout.html"), name="logout"
    ),
    path("", include("clientes.urls")),
]
