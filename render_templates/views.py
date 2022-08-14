from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import functions as f


# Create your views here.


def home(request):
    return render(request, "render_templates/index.html")


@login_required(login_url="/home/")
def billetera(request):
    if not request.user.is_authenticated:
        home(request)
    dni = request.user.username

    context = f.get_user_info(dni)

    return render(
        request,
        "render_templates/billetera.html",
        {"name": request.user.first_name, **context},
    )


@login_required(login_url="/home/")
def tubanco(request):
    if not request.user.is_authenticated:
        home(request)
    dni = request.user.username

    context = f.get_user_info(dni)

    return render(request, "render_templates/tubanco.html", {**context})


@login_required(login_url="/home/")
def compraventausd(request):
    if not request.user.is_authenticated:
        home(request)
    return render(request, "render_templates/compraventausd.html")


@login_required(login_url="/home/")
def graficos(request):
    if not request.user.is_authenticated:
        home(request)
    return render(request, "render_templates/graficos.html")
