from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.

def index(req):
    if req.method == "POST":
        loginForm = forms.LoginForm(req.POST);
        if loginForm.is_valid():
            print("Input data is valid ! ")
        else:
            print("Input data is invalid ! ")
        
    else:
        loginForm = forms.LoginForm();
    return render(req, "ArbitrageApp/LoginForm.html", {"loginForm":loginForm});