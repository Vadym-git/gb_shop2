from django.db import models
from string import ascii_letters
from random import choice
from django.contrib.auth.models import User


class UserModel(models.Model):
    user = models.OneToOneField(User, verbose_name='User', on_delete=models.CASCADE, unique=True)
    phone_number = models.CharField(verbose_name='Phone number', max_length=17, default='', blank=True)
    address = models.CharField(verbose_name='Address', max_length=50, blank=True)
    address2 = models.CharField(verbose_name='Address line 2', max_length=50, blank=True)
    zipcode = models.CharField(verbose_name='Post index', max_length=8, blank=True)
    city = models.CharField(verbose_name='City', max_length=50, blank=True)
    state = models.CharField(verbose_name='State', max_length=50, blank=True)
    country = models.CharField(verbose_name='User county', max_length=50, blank=True)
    activation_link = models.TextField(blank=True)

    @staticmethod
    def new_link(length=12):
        link_string = ''.join(choice(ascii_letters) for _ in range(length))
        return link_string

    @staticmethod
    def activation_user(link):
        user = UserModel.objects.get(activation_link=link)
        if user:
            user.active = True
            user.save()
            return user.user
        return False

    def __str__(self):
        return self.user.first_name

