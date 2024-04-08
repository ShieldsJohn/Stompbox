from django.shortcuts import render
from django.views import generic
from .models import Category


# Create your views here.
# class Base(generic.ListView):
   # model = Category
   # template_name = "listings/base.html"

def base(request):
    return render(request, "listings/base.html")

def home(request):
    return render(request, "listings/home.html")

def myaccount(request):
    return render(request, "listings/myaccount.html")