from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.

def loginView(req):

    if req.method == "POST":
        loginForm = forms.LoginForm(req.POST);
        if loginForm.is_valid():
            print("Input data is valid ! ")
            usr = loginForm.cleaned_data.get("username");
            pswd = loginForm.cleaned_data.get("password");
            usrInDB = authenticate(username=usr, password=pswd)
            if usrInDB is not None :
                print("User is authenticated !");
                login(req, usrInDB);
                return redirect("index");
            else:
                print("Wrong username or password ");

        else:
            print("Input data is invalid ! ")
        
    else:
        loginForm = forms.LoginForm();
    return render(req, "ArbitrageApp/LoginForm.html", {"loginForm":loginForm});

@login_required
def indexView(req):
    return render(req, "ArbitrageApp/Hellopage.html");