from django import forms
from django.core import validators






class LoginForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Phone number'}),
                            validators=[validators.MaxLengthValidator(11), validators.MinLengthValidator(11)])
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Password'}),
                               validators=[validators.MinLengthValidator(4)])

class RegisterForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Phone number'}),
                            validators=[validators.MaxLengthValidator(11), validators.MinLengthValidator(11)])
