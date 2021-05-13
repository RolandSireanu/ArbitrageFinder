
from django.urls import path
from ArbitrageApp import views

urlpatterns = [
    path('Login', views.index, name="index")
];