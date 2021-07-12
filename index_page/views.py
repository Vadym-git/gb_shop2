from django.shortcuts import render
from .models import Products


def index(request):
    products = Products.objects.all()
    return render(request, "index.html", context={'products': products

    })