from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('register', views.OtpLoginView.as_view(), name='register'),
    path('login', views.LoginView.as_view(), name='login'),
    path('checkotp', views.CheckOptView.as_view(), name='check_otp'),
    path('logout', views.LogoutView.as_view(), name='logout'),
]