from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.


def home(request):
    return render(request, "render_templates/index.html")


@login_required(login_url="/home/")
def billetera(request):
    if not request.user.is_authenticated:
        home(request)

    return render(request, "render_templates/billetera.html")
