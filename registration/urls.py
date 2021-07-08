from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='registration'),
    path('reg/<slug:slug>/', views.confirmation_reg, name='confirmation'),
    path('reg/', views.confirmation_reg, name='confirmation'),
]