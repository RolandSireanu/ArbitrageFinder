from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.

def index(req):
    loginForm = forms.LoginForm();
    return render(req, "ArbitrageApp/LoginForm.html", {"loginForm":loginForm});