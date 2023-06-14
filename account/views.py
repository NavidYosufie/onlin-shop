from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.views.generic import TemplateView
from django.views import View
from . import forms
import ghasedakpack
from random import randint
import uuid
from .models import Otp, User

sms = ghasedakpack.Ghasedak("16e061d580d3128b17f425aee0a4be090e5e7bfc11e3a02c9c80f1d6c5961e65")

class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, 'account/login.html', {'form': form})

    def post(self, request):
        form = forms.LoginForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['phone'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error('phone', 'in valid phone')
        else:
            form.add_error('phone', 'this information is wrung')

        return render(request, 'account/login.html', {'form': form})


class OtpLoginView(View):
    def get(self, request):
        form = forms.OtpLoginForm()
        return render(request, 'account/register.html', {'form': form})

    def post(self, request):
        form = forms.OtpLoginForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            randcode = randint(1000, 9999)
            sms.verification({'receptor': cd['phone'], 'type': '1', 'template': 'code', 'param1': randcode})
            token = uuid.uuid4()
            print(randcode)
            Otp.objects.create(phone=cd['phone'], code=randcode, token=token)
            return redirect(reverse('account:check_otp') + f'?token={token}')

        return render(request, 'account/register.html', {'form': form})


class CheckOptView(View):
    def get(self, request):
        form = forms.CheckOtpForm()
        return render(request, 'account/check_opt.html', {'form': form})

    def post(self, request):
        token = request.GET.get("token")
        form = forms.CheckOtpForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if Otp.objects.filter(code=cd['code'], token=token).exists():
                otp = Otp.objects.get(token=token)
                user, is_created = User.objects.get_or_create(phone=otp.phone)
                login(request, user)
                otp.delete()
                return redirect('/')
            else:
                form.add_error('code', 'this code is wrung')

        return render(request, 'account/check_opt.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')
