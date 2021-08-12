from django.db import models
from datetime import datetime
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model

# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name} - ₹{self.price}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self) -> str:
        stfsts = ""
        if self.is_staff:
            stfsts = "(STAFF)"
        return f"{str(self.user.first_name)} {str(self.user.last_name)} - Profile {stfsts}"


class Order(models.Model):
    custormer_phone_no = models.IntegerField(max_length=15)

    order_json = models.JSONField(null=True) # {"<Product ID>": <No. of items>} eg. {"2": 3, "1": 2}
    time_of_order = models.DateTimeField()
    time_of_delivery = models.DateTimeField()

    time_created = models.DateTimeField(auto_now_add=True)

    total_bill = models.IntegerField(default=0)
    bill_text = models.TextField(default="", blank=True)

    discount = models.IntegerField(default=0)

    

    def save(self, *args, **kwargs):

        bill = 0
        bill_text = ''

        for product_id in self.order_json:
            product = Product.objects.get(id=product_id)
            bill += product.price * self.order_json[product_id]

            bill_text += f'{product.name} (₹{product.price}) [x{self.order_json[product_id]}] - ₹{product.price * self.order_json[product_id]}\n'

        self.total_bill = bill
        self.bill_text = bill_text


        super(Order, self).save(*args, **kwargs)
    
    
    def __str__(self) -> str:
        return f"₹{self.total_bill} - ₹{self.discount} >> {(self.time_of_delivery.strftime('%d/%m/%y, %H:%M'))}"


class Expense(models.Model):

    time_created = models.DateTimeField(auto_now_add=True)
    time_of_expense = models.DateTimeField()

    amount = models.IntegerField()

    summary = models.CharField(max_length=150, null=True, blank=True)

class Customer(models.Model):
    name = models.CharField(max_length=70)
    phone_no = models.IntegerField(max_length=15)