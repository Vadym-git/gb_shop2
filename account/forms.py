from django import forms
from django.contrib.auth.models import User


class ContactForm(forms.Form):
    first_name = forms.CharField(label='Name', required=True)
    last_name = forms.CharField(label='Last Name', required=True)
    email = forms.EmailField(label='Email', required=True)
    phone = forms.CharField(label='Phone number', required=False)
    address = forms.CharField(label='Address', required=True)
    address2 = forms.CharField(label='Address 2', required=False)
    zipcode = forms.CharField(label='ZIP CODE / Index', required=True)
    city = forms.CharField(label='City', required=True)
    state = forms.CharField(label='State', required=False)
    country = forms.CharField(label='Country', required=True)


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(), required=True)