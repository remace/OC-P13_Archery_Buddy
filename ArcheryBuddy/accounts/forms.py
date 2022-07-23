from django import forms


class LoginForm(forms.Form):
    pseudo = forms.CharField(label="pseudo", max_length=32)
    password = forms.CharField(label="password", widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    pseudo = forms.CharField(label="pseudo", max_length=32)
    password = forms.CharField(label="password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="password", widget=forms.PasswordInput())
    first_name = forms.CharField(label="prénom", max_length=32)
    last_name = forms.CharField(label="nom", max_length=32)
    email = forms.EmailField(label="email")
