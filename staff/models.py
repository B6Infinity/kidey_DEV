from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=50)
    price = models.IntegerField()

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

    