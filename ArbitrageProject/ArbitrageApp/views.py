from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import forms
# Create your views here.

def loginView(req):

    notification = None;

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
                notification = "Wrong username or password ";
                print("Wrong username or password ");

        else:
            print("Input data is invalid ! ")
        
    else:
        loginForm = forms.LoginForm();
    return render(req, "ArbitrageApp/LoginForm.html", {"loginForm":loginForm, "notification":notification});

def logoutView(req):
    logout(req);
    return redirect("login");

def registerView(req):
    if(req.method == "POST"):
        registerForm = forms.RegisterForm(req.POST)
        if registerForm.is_valid():
            print("Register data is valid ! ");
            usr = registerForm.cleaned_data.get("username");
            pswd = registerForm.cleaned_data.get("password");
            conf_pswd = registerForm.cleaned_data.get("conf_password");
            User.objects.create_user(username=usr,password=pswd);

            print(usr,pswd,conf_pswd);
            return redirect("login");
        else:
            pass
    else:
        registerForm = forms.RegisterForm();

    return render(req, "ArbitrageApp/RegisterAccount.html", {"registerForm":registerForm})

@login_required(redirect_field_name=None)
def indexView(req):
    return render(req, "ArbitrageApp/index.html");