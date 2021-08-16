from django.core.checks.messages import ERROR
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *
import json

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
    
    if request.method == 'POST' and request.user.is_staff:
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
    if request.method == 'POST' and request.user.is_staff:
        product_id = request.POST['product_id']

        if len(Product.objects.filter(id=product_id)) != 0:
            del_product = Product.objects.get(id=product_id)
            del_product.delete()

        return HttpResponse("<h1>Product Successfully Deleted! <a href='/staff/products'>Back</a></h1>")

    else:
        return HttpResponse("Critical Gateway! Data Loss!")

def addOrder(request):
    if request.method == 'POST' and request.user.is_staff:
        customer_name = request.POST['customer_name']
        customer_phone_no = request.POST['customer_phone_no']
        
        time_of_order = request.POST['time_of_order']
        time_of_delivery = request.POST['time_of_delivery']
        discount = request.POST['discount']
        order_json = request.POST['order_json']

        # Frisk Data
        if len(discount) == 0:
            discount = "0"
        


        # Handling the Customer
        __customer = Customer.objects.get_or_create(name=customer_name, phone_no=customer_phone_no)
        customer = __customer[0]

        # Handling the Order
        newOrder = Order.objects.create(
            customer = customer, 
            order_json = json.loads(order_json), 
            time_of_order = datetime.strptime(time_of_order, "%Y-%m-%dT%H:%M"),
            time_of_delivery = datetime.strptime(time_of_delivery, "%Y-%m-%dT%H:%M"),
            discount = int(discount)
        )


        return HttpResponse("<h1>Order Successfully Created! <a href='/staff/orders'>Back</a></h1>")

    else:
        return HttpResponse("Critical Gateway! Data Loss!")


# APIs

def fetchCustomer(request):
    
    if request.method == 'POST' and request.user.is_staff:
        datatype = request.POST['datatype']
        data = request.POST['data']
        RESPONSE = {"ERROR": None}


        if datatype == 'name':
            name = data.lower()
            if len(Customer.objects.filter(name__iexact=name)) == 0:
                RESPONSE["ERROR"] = "NOT FOUND"
            else:
                matching_customer = Customer.objects.filter(name__iexact=name)[0]
                RESPONSE["MATCHING_CUSTOMER"] = {"Name": matching_customer.name, "Phone": matching_customer.phone_no}

        elif datatype == 'phone_no':
            
            phone_no = data.lower()
            if len(Customer.objects.filter(phone_no=phone_no)) == 0:
                RESPONSE["ERROR"] = "NOT FOUND"
            else:
                matching_customer = Customer.objects.filter(phone_no=phone_no)[0]
                RESPONSE["MATCHING_CUSTOMER"] = {"Name": matching_customer.name, "Phone": matching_customer.phone_no}
            

        else:
            RESPONSE["ERROR"] = "Invalid 'datatype' parameter"
        
        return JsonResponse(RESPONSE)
    
    else:
        return HttpResponse("Not this way Mr. heckar :)")

def fetchOrder(request):
    if request.method == 'POST' and request.user.is_staff:
        RESPONSE = {"ERROR": None}
        
        order_id = request.POST['order_id']

        if len(Order.objects.filter(id=order_id)) == 0:
            RESPONSE["ERROR"] = "Order does not exist!"
        else:
            order = Order.objects.get(id=order_id)

            RESPONSE["ORDER"] = {
                "NAME": order.customer.name,
                "PHONE": order.customer.phone_no,
                "ADDRESS": order.customer.address,
                "BILL_TEXT": order.bill_text,
                "TIME_OF_ORDER": order.time_of_order.date(),
                "TIME_OF_DELIVERY": order.time_of_delivery.strftime("%d/%m/%Y %-I:%M %p"),
            }
        
        return JsonResponse(RESPONSE)

