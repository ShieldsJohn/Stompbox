from django.shortcuts import render
from django.views import generic
from .models import Category

def myaccount(request):
    return render(request, "listings/myaccount.html")