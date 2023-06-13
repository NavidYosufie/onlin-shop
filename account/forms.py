from django import forms
from django.core import validators
from django.core.exceptions import ValidationError

from account.models import User


class LoginForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Phone number'}),
                            validators=[validators.MaxLengthValidator(11), validators.MinLengthValidator(11)])
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Password'}),
                               validators=[validators.MinLengthValidator(4)])

class OtpLoginForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Phone number'}),
                            validators=[validators.MaxLengthValidator(11), validators.MinLengthValidator(11)])


class CheckOtpForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Code'}),
                            validators=[validators.MaxLengthValidator(4), validators.MinLengthValidator(4)])

