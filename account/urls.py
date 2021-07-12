from django.urls import path

from . import views

urlpatterns = [
    path('', views.account, name='registration'),
    path('logout/', views.log_out, name='logout'),
]