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

    existing_orders = Order.objects.all()
    DATA["EXISTING_ORDERS"] = existing_orders

    existing_products = Product.objects.all()
    DATA["EXISTING_PRODUCTS"] = existing_products


    return render(request, 'staff/orders.html', DATA)

def money(request):
    if not request.user.is_staff:
        return HttpResponse("You need to login as a staff <a href='/staff'>Login Here</a>")
    
    DATA = {"CURRENT_PAGE": "money"}
    return render(request, 'staff/money.html', DATA)

def addProduct(request):
    
    if request.method == 'POST':
        new_product = request.POST['new_product']
        
        if new_product == "false":
            # Edit Product

            product_id = request.POST['product_id']

            if len(Product.objects.filter(id=product_id)) != 0:
                edit_product = Product.objects.get(id=product_id)
                
                product_name = request.POST['product_name']
                price = request.POST['price']

                edit_product.name = product_name
                edit_product.price = price
                edit_product.save()

                return HttpResponse("<h1>Product Successfully Edited! <a href='/staff/products'>Back</a></h1>")

            else:
                # PRODUCT DOES NOT EXIST
                return HttpResponse("Product Does not exist! <a href='/staff/products'>Back</a>")
        
        else:
            # Create Product

            product_name = request.POST['product_name']
            price = request.POST['price']

            Product.objects.create(name=product_name, price=price)

            return HttpResponse("<h1>Product Successfully Created! <a href='/staff/products'>Back</a></h1>")

        

    else:
        return HttpResponse("Critical Violation... Invalid Gateway!")

def deleteProduct(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']

        if len(Product.objects.filter(id=product_id)) != 0:
            del_product = Product.objects.get(id=product_id)
            del_product.delete()

        return HttpResponse("<h1>Product Successfully Deleted! <a href='/staff/products'>Back</a></h1>")

    else:
        return HttpResponse("Critical Gateway! Data Loss!")

# APIs

