import datetime
from datetime import date, timedelta
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
        
    existing_products = Product.objects.all()[::-1]
    DATA["EXISTING_PRODUCTS"] = existing_products


    categories = []
    for product in existing_products:
        if product.category not in categories:
            categories.append(product.category)

    DATA["CATEGORIES"] = categories[::-1]

    return render(request, 'staff/products.html', DATA)

def analytics(request):
    if not request.user.is_staff:
        return HttpResponse("You need to login as a staff <a href='/staff'>Login Here</a>")

    DATA = {"CURRENT_PAGE": "analytics"}

    # Data to send: Last Week Sales,

    seven_days_before = date.today() - timedelta(days=6)

    # MONDAY IS '0'
    weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    LAST_WEEK_SALES = [] # Labels(Day), Data
    # Fetch Last Week Orders
    last_week_orders = Order.objects.filter(time_of_order__gte=seven_days_before, paid=True)
    startingDay = seven_days_before.weekday()
    LAST_WEEK_SALES.append(weekDays[startingDay:] + weekDays[:startingDay])
    
    
    JS = {}
    for day in LAST_WEEK_SALES[0]:
        JS[day] = 0
    
    for order in last_week_orders:
        Oday = weekDays[order.time_of_order.weekday()]
        JS[Oday] += order.payable_amt
    
    LAST_WEEK_SALES.append(list(JS.values()))
    startingDay = seven_days_before.weekday()

    LAST_WEEK_EXPENSES = [] # Labels(Day), Data

    last_week_expenses = Expense.objects.filter(time_of_expense__gte=seven_days_before)
    startingDay = seven_days_before.weekday()
    LAST_WEEK_EXPENSES.append(weekDays[startingDay:] + weekDays[:startingDay])
    
    
    JS = {}
    for day in LAST_WEEK_EXPENSES[0]:
        JS[day] = 0
    
    for expense in last_week_expenses:
        Oday = weekDays[expense.time_of_expense.weekday()]
        JS[Oday] += expense.amount


    LAST_WEEK_EXPENSES.append(list(JS.values()))

    DATA["LAST_WEEK_SALES"] = LAST_WEEK_SALES
    DATA["LAST_WEEK_EXPENSES"] = LAST_WEEK_EXPENSES

    startingDay = seven_days_before.weekday()


    MOST_ORDERED_PRODUCTS = []

    JS = {}
    for order in last_week_orders:
        order_json = order.order_json
        for product in order_json:
            product_name = Product.objects.get(id=product).name
            if not product_name in JS:
                JS[product_name] = 0
            JS[product_name] += order_json[product]

    MOST_ORDERED_PRODUCTS.append(list(JS.keys()))
    MOST_ORDERED_PRODUCTS.append(list(JS.values()))
    DATA["MOST_ORDERED_PRODUCTS"] = MOST_ORDERED_PRODUCTS




    return render(request, 'staff/analytics.html', DATA)

def orders(request):
    if not request.user.is_staff:
        return HttpResponse("You need to login as a staff <a href='/staff'>Login Here</a>")

    DATA = {"CURRENT_PAGE": "orders"}

    existing_orders = Order.objects.all()
    DATA["EXISTING_ORDERS"] = existing_orders[::-1]

    existing_products = Product.objects.all()
    DATA["EXISTING_PRODUCTS"] = existing_products



    categories = []
    for product in existing_products:
        if product.category not in categories:
            categories.append(product.category)

    # Making Sure that 'NONE' Category appears in the end
    
    categories.remove(categories[categories.index("none")])
    categories.append("none")
    DATA["CATEGORIES"] = categories


    return render(request, 'staff/orders.html', DATA)

def money(request):
    if not request.user.is_staff:
        return HttpResponse("You need to login as a staff <a href='/staff'>Login Here</a>")

    
    
    DATA = {"CURRENT_PAGE": "money", "CASH": Money.objects.all()[0], "EXPENSES":Expense.objects.all()[:20][::-1]}
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
                category = request.POST['category']

                edit_product.name = product_name
                edit_product.price = price
                edit_product.category = category
                edit_product.save()

                return redirect("products")

            else:
                # PRODUCT DOES NOT EXIST
                return HttpResponse("Product Does not exist! <a href='/staff/products'>Back</a>")
        
        else:
            # Create Product

            product_name = request.POST['product_name']
            price = request.POST['price']
            category = request.POST['category']

            Product.objects.create(name=product_name, price=price, category=category)

            return redirect("products")

        

    else:
        return HttpResponse("Critical Violation... Invalid Gateway!")

def deleteProduct(request):
    if request.method == 'POST' and request.user.is_staff:
        product_id = request.POST['product_id']

        if len(Product.objects.filter(id=product_id)) != 0:
            del_product = Product.objects.get(id=product_id)
            del_product.delete()

        return redirect("products")

    else:
        return HttpResponse("Critical Gateway! Data Loss!")

def addOrder(request):
    if request.method == 'POST' and request.user.is_staff:
        customer_name = request.POST['customer_name']
        customer_phone_no = request.POST['customer_phone_no']
        address = request.POST['customer_address']        
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

        customer.address = address
        customer.save()

        return redirect("orders")

    else:
        return HttpResponse("Critical Gateway! Data Loss!")

def deleteOrder(request):
    if request.method == 'POST' and request.user.is_staff:
        order_id = request.POST['order-id']
        
        # DELETE THE ORDER

        if len(Order.objects.filter(id=order_id)) != 0:
            del_order = Order.objects.get(id=order_id)
            del_order.delete()

        return redirect("orders")

    else:
        return HttpResponse("Critical Gateway! Data Loss!")

def withdrawMoney(request):
    if request.method == 'POST' and request.user.is_staff:
        withdraw_name = request.POST['withdraw_name']
        withdraw_amt = request.POST['withdraw_amt']
        withdraw_summary = request.POST['withdraw_summary']
        time_of_expense = request.POST['widthdraw_time']

        Expense.objects.create(withdrawer=withdraw_name, amount=int(withdraw_amt), summary=withdraw_summary, time_of_expense=time_of_expense)

        return redirect("money")

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
                RESPONSE["MATCHING_CUSTOMER"] = {"Name": matching_customer.name, "Phone": matching_customer.phone_no, "Address": matching_customer.address}

        elif datatype == 'phone_no':
            
            phone_no = data.lower()
            if len(Customer.objects.filter(phone_no=phone_no)) == 0:
                RESPONSE["ERROR"] = "NOT FOUND"
            else:
                matching_customer = Customer.objects.filter(phone_no=phone_no)[0]
                RESPONSE["MATCHING_CUSTOMER"] = {"Name": matching_customer.name, "Phone": matching_customer.phone_no, "Address": matching_customer.address}
            

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
                "PAID": order.paid,
                "MONEY": f"₹{order.total_bill} - ₹{order.discount} => <span style='color: lime; font-size:25px; font-weight:900;'>₹{order.payable_amt}/-</span>",
                "TIME_OF_ORDER": order.time_of_order.strftime("%b. %d, %-I:%M %p"),
                "TIME_OF_DELIVERY": order.time_of_delivery.strftime("%b. %d, %-I:%M %p"),
            }
        
        return JsonResponse(RESPONSE)

def markOrderPaid(request):
    if request.method == 'POST' and request.user.is_staff:
        RESPONSE = {"ERROR": None}
        
        order_id = request.POST['order_id']

        if len(Order.objects.filter(id=order_id)) == 0:
            RESPONSE["ERROR"] = "Order does not exist!"
        else:
            order = Order.objects.get(id=order_id)
            order.paid = True
            order.save()

        return JsonResponse(RESPONSE)


# STATICITY

def get_menu(request):
    return HttpResponse("HI")