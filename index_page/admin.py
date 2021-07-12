from django.contrib import admin
from .models import Products, ProductCategory


@admin.register(Products)
class AdminProduct(admin.ModelAdmin):
    save_on_top = True


@admin.register(ProductCategory)
class AdminProductCategory(admin.ModelAdmin):
    save_on_top = True