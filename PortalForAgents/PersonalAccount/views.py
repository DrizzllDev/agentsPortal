from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


def registrationPage(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, 'PersonalAccount/registration.html',{'form' : form})

def loginPage(request):
    return render(request, 'PersonalAccount/login.html')
