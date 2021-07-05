from django.db import models
from string import ascii_letters
from random import choice


# Я нарошно не наследуюсь от стандартного класса User
class UserModel(models.Model):
    name = models.EmailField(max_length=32, unique=True)
    password = models.CharField(max_length=128)
    activation_link = models.TextField()
    active = models.BooleanField(default=False)

    @staticmethod
    def new_link(lenght=12):
        link_string = ''.join(choice(ascii_letters) for _ in range(lenght))
        return link_string

    @staticmethod
    def check_registration(email):
        user = UserModel.objects.filter(name=email)
        return True if user else False

    @staticmethod
    def activation_user(link):
        user = UserModel.objects.get(activation_link=link)
        if user:
            user.active = True
            user.save()
            return True
        return False

    def __str__(self):
        return self.name

