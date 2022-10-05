from django.contrib import admin
from django.urls import path
from .views import registrationPage, loginPage

urlpatterns = [
    path('registration', registrationPage, name='registrationPage'),
    path('login', loginPage, name='loginPage'),
]
