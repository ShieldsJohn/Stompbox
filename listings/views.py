from django.shortcuts import render
from django.views import generic
from .models import Category


# Create your views here.
class Index(generic.ListView):
    model = Category
    template_name = "listings/index.html"
