from django.shortcuts import render
from django.http import HttpResponse
import allauth.socialaccount.views as v1


def index(request):
    return render(request, "index.html")
