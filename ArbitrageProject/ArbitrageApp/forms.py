from django import forms
from django.forms.fields import MultiValueField
from .LoginFormValidation import validateLength, validateStartCharacterDigit, validateWhiteSpaces
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "id":"login", "class":"fadeIn second", "name":"login", "placeholder":"username", "type":"text" }
    ), validators=[validateWhiteSpaces]);
    password = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "id":"password", "class":"fadeIn third", "name":"login", "placeholder":"password", "type":"password" }
    ),validators=[validateWhiteSpaces]);
    
    def clean(self):
        cleaned_data = super(LoginForm, self).clean();
        username = cleaned_data.get("username");
        password = cleaned_data.get("password");
        
        if "username" not in cleaned_data:
            self.fields["username"].widget.attrs["class"] += " form-control is-invalid";
        if "password" not in cleaned_data:
            self.fields["password"].widget.attrs["class"] += " form-control is-invalid";
        
class RegisterForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "id":"login", "class":"fadeIn second", "name":"login", "placeholder":"username", "type":"text" }
    ), validators=[validateLength(3), validateStartCharacterDigit, validateWhiteSpaces]);

    password = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "id":"password", "class":"fadeIn third", "name":"login", "placeholder":"password", "type":"password" }),
        validators=[validateLength(4), validateWhiteSpaces]);

    conf_password = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "id":"password", "class":"fadeIn third", "name":"login", "placeholder":"confirm password", "type":"password" }),
        validators=[validateLength(4), validateWhiteSpaces]);
        

    def clean_conf_password(self):
        pass1 = self.cleaned_data.get("password");
        pass2 = self.cleaned_data.get("conf_password");

        if(pass1 != pass2):
            raise ValidationError("Passwords doesn't match !");
        else:
            return pass2;


            