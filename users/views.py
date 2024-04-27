from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.models import User
from .forms import UserForm

# Render myaccount page if logged in
@login_required
def myaccount(request):
    return render(request, "myaccount.html")

def profile_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_form_success')
    else:
        form = UserForm()
    return render(request, 'profile_form.html', {'form': form})

# Render view_myaccount if logged in
@login_required
def view_myaccount(request):
    user = request.user
    return render(request, 'view_myaccount.html', {'user': user})

# Render profile_form_success if logged in
@login_required
def profile_form_success(request):
    user = request.user
    return render(request, 'profile_form_success.html', {'user': user})
