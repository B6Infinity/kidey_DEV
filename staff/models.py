from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

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
    products = models.ManyToManyField(Product, related_name='orders')
    time_of_order = models.DateTimeField()
    time_of_delivery = models.DateTimeField()

    total_bill = models.IntegerField(default=0)

    discount = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{len(self.products)} Products - ₹{self.total_bill} - ₹{self.discount}"
    