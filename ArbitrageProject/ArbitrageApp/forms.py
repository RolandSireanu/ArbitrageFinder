from django import forms
from .LoginFormValidation import LoginUsernameAsserts, LoginUsernameMsgs


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "id":"login", "class":"fadeIn second", "name":"login", "placeholder":"username", "type":"text" }
    ));
    password = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "id":"password", "class":"fadeIn third", "name":"login", "placeholder":"password", "type":"password" }));
    
    def clean(self):
        cleaned_data = super(LoginForm, self).clean();
        username = cleaned_data.get("username");
        password = cleaned_data.get("password");
        
        if "username" not in cleaned_data:
            self.fields["username"].widget.attrs["class"] += " form-control is-invalid";
        if "password" not in cleaned_data:
            self.fields["password"].widget.attrs["class"] += " form-control is-invalid";
        

    def clean_username(self):
        usr = self.cleaned_data.get("username");

        if any([asrt(usr) for asrt in LoginUsernameAsserts]) :
            for idx, asrt in enumerate(LoginUsernameAsserts):
                if asrt(usr) :
                    self.fields["username"].widget.attrs["class"] += " form-control is-invalid";
                    raise forms.ValidationError(LoginUsernameMsgs[idx]);
        return usr;

    def clean_password(self):
        pswd = self.cleaned_data.get("password");
        if len(pswd) < 4:
            self.fields["password"].widget.attrs["class"] += " form-control is-invalid";
            raise forms.ValidationError("Password should be at least 4 characters long");
            