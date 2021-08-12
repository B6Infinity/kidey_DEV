from django.contrib import admin
from .models import Product, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Product)