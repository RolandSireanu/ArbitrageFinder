from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(min_length=3, required=True, widget=forms.TextInput(attrs={
        "id":"login", "class":"fadeIn second", "name":"login", "placeholder":"username" }
    ));
    password = forms.CharField(min_length=4, required=True, widget=forms.TextInput(attrs={
        "id":"password", "class":"fadeIn third", "name":"login", "placeholder":"password" }));
    