from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('saveCustomers/', views.saveCustomers, name="saveCustomers"),
    path('saveProduct/', views.saveProduct, name="saveProduct"),
    path('newOrderForm/', views.newOrderForm, name="newOrderForm"),
    path('saveFinalOrder/', views.saveFinalOrder, name="saveFinalOrder"),

]
