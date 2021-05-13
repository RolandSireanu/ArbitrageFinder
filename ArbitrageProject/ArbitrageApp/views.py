from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from . import forms
# Create your views here.

def index(req):

    if req.method == "POST":
        loginForm = forms.LoginForm(req.POST);
        if loginForm.is_valid():
            print("Input data is valid ! ")
            usr = loginForm.cleaned_data.get("username");
            pswd = loginForm.cleaned_data.get("password");
            usrInDB = authenticate(username=usr, password=pswd)
            if usrInDB is not None :
                print("User is authenticated !");
                return redirect("/Hello");
            else:
                print("Wrong username or password ");

        else:
            print("Input data is invalid ! ")
        
    else:
        loginForm = forms.LoginForm();
    return render(req, "ArbitrageApp/LoginForm.html", {"loginForm":loginForm});


def hello(req):
    return render(req, "ArbitrageApp/Hellopage.html");