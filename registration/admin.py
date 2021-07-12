from django.contrib import admin
from .models import UserModel


@admin.register(UserModel)
class AdminUserModel(admin.ModelAdmin):
    save_on_top = True
    readonly_fields = ['user',]
