from django.db import models
from string import ascii_letters
from random import choice
from django.contrib.auth.models import User


# Я нарошно не наследуюсь от стандартного класса User
class UserModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=250, null=True, blank=True)
    activation_link = models.TextField()

    @staticmethod
    def new_link(lenght=12):
        link_string = ''.join(choice(ascii_letters) for _ in range(lenght))
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

