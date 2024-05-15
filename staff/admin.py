from django.contrib import admin
from .models import Product, Profile, Order, DeliveryLandmark, Expense, Customer, Money, GlobalVariable

# Register your models here.
admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(DeliveryLandmark)
admin.site.register(Expense)
admin.site.register(Customer)
admin.site.register(Money)
admin.site.register(GlobalVariable)