from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from django.views import View
from . import forms

class Login(View):
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




