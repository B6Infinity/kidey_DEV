import json
from django.db import models
from datetime import datetime
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import CharField, TextField

from subtle_defs import printC

# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=50)
    price = models.IntegerField()

    category_choices = (
        ('none', 'none'),
        ('biriyani', 'biriyani'),
        ('thali', 'thali'),
        ('extra', 'extra'),
        ('chinese', 'chinese'),
        ('curry', 'curry'),
    )
    
    category = models.CharField(max_length=25, choices=category_choices, default='none')

    def __str__(self) -> str:
        return f"{self.name} - ₹{self.price}"
    
    def get_all_categories(self) -> tuple:
        return self.category_choices


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self) -> str:
        stfsts = ""
        if self.is_staff:
            stfsts = "(STAFF)"
        return f"{str(self.user.first_name)} {str(self.user.last_name)} - Profile {stfsts}"


class Customer(models.Model):
    name = models.CharField(max_length=120)
    phone_no =  models.IntegerField()

    address = models.TextField(default="")

    def __str__(self) -> str:
        return f"{self.name}({self.phone_no})"


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name="placed_orders")


    order_json = models.TextField() # {"<Product ID>": <No. of items>} eg. {"2": 3, "1": 2}
    time_of_order = models.DateTimeField()
    time_of_delivery = models.DateTimeField()

    time_created = models.DateTimeField(auto_now_add=True)

    delivery_charge = models.IntegerField(default=0)

    discount = models.IntegerField(default=0)
    total_bill = models.IntegerField(default=0)
    payable_amt = models.IntegerField(default=0, blank=True)

    bill_text = models.TextField(default="", blank=True)
    
    paid = models.BooleanField(default=False)

    def save(self, *args, **kwargs):

        bill = 0
        bill_text = ''

        
        self.order_json = self.order_json.replace('\'', '"')
        order_json = json.loads(self.order_json)
        
        # Evaluate Product Cost
        for product_id in order_json:
            product = Product.objects.get(id=product_id)
            bill += product.price * order_json[product_id]

            bill_text += f'{product.name} (₹{product.price}) [x{order_json[product_id]}] - ₹{product.price * order_json[product_id]}/-\n'


        self.total_bill = bill
        self.payable_amt = bill + self.delivery_charge - self.discount
        self.bill_text = bill_text

        if self.paid:
            # Online or Offline

            if len(kwargs) == 0:
                index = 0
            elif kwargs["is_online"]:
                index = 1
            else:
                index = 0

            printC(f"Pushing in {['CASH', 'ONLINE'][index]}")
            
            m = Money.objects.all()[index]
            m.value += self.payable_amt
            m.save()

            # Clear kwargs
            kwargs = {}


        super(Order, self).save(*args, **kwargs)
    
    def get_unpaid(self, *args, **kwargs):
        return ['BAL']
    
    def __str__(self) -> str:
        return f"{self.customer}:₹{self.payable_amt} >> {(self.time_of_delivery.strftime('%d/%m/%y, %H:%M'))}"


class DeliveryLandmark(models.Model):
    name = models.CharField(max_length=30)
    distance = models.FloatField()
    time_in_minutes = models.IntegerField()

    parent = models.CharField(max_length=30, default="Barasat", blank=True)

    # charge = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.parent} - {self.name}"

    # def save(self, *args, **kwargs):
        
        
        
    #     super(Order, self).save(*args, **kwargs)



class Expense(models.Model): # '0' is CASH and '1' is ONLINE

    withdrawer = models.CharField(max_length=150, default="", null=True, blank=True)

    time_created = models.DateTimeField(auto_now_add=True)
    time_of_expense = models.DateTimeField()

    amount = models.IntegerField()
    is_online = models.BooleanField(default=False)

    summary = models.TextField(null=True, blank=True)


    def save(self, *args, **kwargs):

        if self.is_online:
            m = Money.objects.all()[1]
            m.value -= self.amount
            m.save()
        else:
            m = Money.objects.all()[0]
            m.value -= self.amount
            m.save()

        super(Expense, self).save(*args, **kwargs)

    def __str__(self) -> str:
        # return f"<b style='color:skyblue;'>₹{self.amount}</b> - {self.time_of_expense.strftime('%d/%m/%y, %H:%M')}"
        return f"₹{self.amount} - {self.time_of_expense.strftime('%d/%m/%y, %H:%M')}"


class Money(models.Model):
    value = models.IntegerField(default=0)
    online_mode = models.BooleanField(default=False)

    def __str__(self) -> str:
        if self.online_mode:
            return "Online"
        else:
            return "Cash"


class GlobalVariable(models.Model):
    name = models.CharField(max_length=20)
    value = models.TextField()

    category_choices = (
        ('none', 'none'),
        ('economic', 'economic'),
        ('delivery_rate', 'delivery_rate'),
        ('constant', 'constant'),
        ('miscellaneous', 'miscellaneous'),
    )
    
    category = models.CharField(max_length=25, choices=category_choices, default='none')

    def __str__(self) -> str:
        return f"[{self.category}]:\t{self.name} = {self.value}"