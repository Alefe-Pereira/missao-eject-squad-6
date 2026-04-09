from django import forms

class LoginForm(forms.Form): #criando as informações necessárias para login
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)