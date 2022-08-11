from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
# Create your views here.


def home(request):
    return render(request, "render_templates/index.html")


def billetera(request):
    return render(request, "render_templates/billetera.html")
