from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "render_templates/index.html")


def billetera(request):
    return render(request, "render_templates/billetera.html")
