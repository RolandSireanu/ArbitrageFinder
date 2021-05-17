
from django.urls import path
from ArbitrageApp import views

urlpatterns = [
    path('Login/', views.loginView, name="login"),
    path("Arbitrage", views.indexView, name="index"),
    path('Logout/', views.logoutView, name="logout"),
    path('register/', views.registerView, name="register")
];