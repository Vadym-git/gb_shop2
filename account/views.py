from django.shortcuts import render, reverse

import index_page.views
from registration.models import UserModel
from django.contrib.auth.models import User
import django.core.exceptions as exceptions
from .forms import ContactForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, response


def account(request):
    message = ''  # left in just in case
    if request.user.is_authenticated:
        if request.method == 'GET':
            user = UserModel.objects.get(user=request.user)
        if request.method == 'POST':
            user = UserModel.objects.get(user=request.user)
            form = ContactForm(request.POST)
            if form.is_valid():
                request.user.first_name = form.cleaned_data['first_name']
                request.user.last_name = form.cleaned_data['last_name']
                request.user.email = form.cleaned_data['email']
                user.phone_number = form.cleaned_data['phone']
                user.address = form.cleaned_data['address']
                user.address2 = form.cleaned_data['address2']
                user.zipcode = form.cleaned_data['zipcode']
                user.city = form.cleaned_data['city']
                user.state = form.cleaned_data['state']
                user.country = form.cleaned_data['country']
                request.user.save()
                user.save()
            else:
                message = 'Form is invalid'
                user = UserModel.objects.get(user=request.user)
        return render(request,
                      "account.html",
                      context={'account': user,
                               'form': ContactForm(initial={'first_name': request.user.first_name,
                                                            'last_name': request.user.last_name,
                                                            'email': request.user.email,
                                                            'phone': user.phone_number,
                                                            'address': user.address,
                                                            'address2': user.address2,
                                                            'zipcode': user.zipcode,
                                                            'city': user.city,
                                                            'state': user.state,
                                                            'country': user.country,
                                                            }),
                               'message': message})
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
                if user is not None:
                    login(request, user)
                    request.session.set_expiry(900)
                    return HttpResponseRedirect(reverse(account))
                message = 'Wrong login or password'
            else:
                message = 'Something wrong with your form'
            return render(request, "account.html", context={'message': message})
        if request.method == 'GET':
            return render(request, "account.html")


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse(index_page.views.index))

