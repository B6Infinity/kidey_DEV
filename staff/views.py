from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *

# Create your views here.
def home(request):
    DATA = {"CURRENT_PAGE": "home"}
    return render(request, 'staff/home.html', DATA)

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

def products(request):
    DATA = {"CURRENT_PAGE": "products"}

    if not request.user.is_staff:
        return HttpResponse("You need to login as a staff <a href='/staff'>Login Here</a>")
        
    existing_products = Product.objects.all()
    DATA["EXISTING_PRODUCTS"] = existing_products


    return render(request, 'staff/products.html', DATA)

def analytics(request):
    if not request.user.is_staff:
        return HttpResponse("You need to login as a staff <a href='/staff'>Login Here</a>")

    DATA = {"CURRENT_PAGE": "analytics"}
    return render(request, 'staff/analytics.html', DATA)

def orders(request):
    if not request.user.is_staff:
        return HttpResponse("You need to login as a staff <a href='/staff'>Login Here</a>")


    DATA = {"CURRENT_PAGE": "orders"}
    return render(request, 'staff/orders.html', DATA)

def money(request):
    if not request.user.is_staff:
        return HttpResponse("You need to login as a staff <a href='/staff'>Login Here</a>")
    
    DATA = {"CURRENT_PAGE": "money"}
    return render(request, 'staff/money.html', DATA)

def addProduct(request):
    pass

# APIs

