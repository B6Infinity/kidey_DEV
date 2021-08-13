from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, 'staff/home.html')

def handle_logout(request):
    logout(request)

    return redirect('home')


def handle_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is None:
            return HttpResponse("Wrong Username or Password <a href='/staff'>Try again!</a>")
        else:
            login(request, user)

        return redirect('home')

    else:
        return HttpResponse("Critical Violation... Login Aborted!")
