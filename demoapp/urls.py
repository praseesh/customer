# from django import views
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [

# path('',views.index),
# path('add',views.addcustomer)
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.addcustomer, name='addcustomer'),
]
