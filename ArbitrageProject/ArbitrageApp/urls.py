
from django.urls import path
from ArbitrageApp import views

urlpatterns = [
    path('', views.index, name="index")
];