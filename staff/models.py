from django.db import models
from datetime import datetime
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import CharField, TextField

# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=50)
    price = models.IntegerField()

    category_choices = (
        ('none', 'none'),
        ('biriyani', 'biriyani'),
        ('thali', 'thali'),
        ('chinese', 'chinese'),
    )
    
    category = models.CharField(max_length=25, choices=category_choices, default='none')

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


class Customer(models.Model):
    name = models.CharField(max_length=120)
    phone_no =  models.IntegerField()

    address = models.TextField(default="")

    def __str__(self) -> str:
        return f"{self.name}({self.phone_no})"


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, related_name="placed_orders")

    order_json = models.JSONField(null=True) # {"<Product ID>": <No. of items>} eg. {"2": 3, "1": 2}
    time_of_order = models.DateTimeField()
    time_of_delivery = models.DateTimeField()

    time_created = models.DateTimeField(auto_now_add=True)

    total_bill = models.IntegerField(default=0)
    bill_text = models.TextField(default="", blank=True)

    discount = models.IntegerField(default=0)

    payable_amt = models.IntegerField(default=0, blank=True)
    
    paid = models.BooleanField(default=False)

    def save(self, *args, **kwargs):

        bill = 0
        bill_text = ''

        for product_id in self.order_json:
            product = Product.objects.get(id=product_id)
            bill += product.price * self.order_json[product_id]

            bill_text += f'{product.name} (₹{product.price}) [x{self.order_json[product_id]}] - ₹{product.price * self.order_json[product_id]}/-\n'

        self.total_bill = bill
        self.payable_amt = bill - self.discount
        self.bill_text = bill_text

        if self.paid:
            m = Money.objects.all()[0]
            m.value += self.payable_amt
            m.save()


        super(Order, self).save(*args, **kwargs)
    
    
    def __str__(self) -> str:
        return f"{self.customer}:₹{self.payable_amt} >> {(self.time_of_delivery.strftime('%d/%m/%y, %H:%M'))}"


class Expense(models.Model):

    withdrawer = models.CharField(max_length=150, default="", null=True, blank=True)

    time_created = models.DateTimeField(auto_now_add=True)
    time_of_expense = models.DateTimeField()

    amount = models.IntegerField()

    summary = models.TextField(null=True, blank=True)


    def save(self, *args, **kwargs):

        m = Money.objects.all()[0]
        m.value -= self.amount
        m.save()

        super(Expense, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"<b style='color:skyblue;'>₹{self.amount}</b> - {self.time_of_expense.strftime('%d/%m/%y, %H:%M')}"

class Money(models.Model):
    value = models.IntegerField(default=0)
