from django.contrib import admin
from .models import Product, Profile, Order, Expense, Customer, Money

# Register your models here.
admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Expense)
admin.site.register(Customer)
admin.site.register(Money)