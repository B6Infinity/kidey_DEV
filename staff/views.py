from django.http.response import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    
    return render(request, 'staff/home.html')