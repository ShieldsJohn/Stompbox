from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views import generic

@login_required
def myaccount(request):
    return render(request, "myaccount.html")
