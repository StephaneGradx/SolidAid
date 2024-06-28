from django.contrib.auth.forms import AuthenticationForm
from  django import forms


class SignupForm(forms.Form):
    nom = forms.CharField(max_length=128)
    password = forms.CharField(widget=forms.PasswordInput)
    type = forms.CharField(max_length=100)
    motif = forms.CharField(max_length=100, widget=forms.Textarea)


class LoginForm(forms.Form):
    nom = forms.CharField(max_length=128)
    password = forms.CharField(widget=forms.PasswordInput)
