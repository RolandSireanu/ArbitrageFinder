
from django.urls import path
from ArbitrageApp import views

urlpatterns = [
    path('login/', views.loginView, name="login"),
    path("Hello", views.indexView, name="index")
];