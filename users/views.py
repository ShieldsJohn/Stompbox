from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.views import generic
from django.contrib.auth.models import User
from .forms import UserForm
from .models import Profile

# Render myaccount page if logged in
@login_required
def myaccount(request):
    return render(request, "myaccount.html")

@login_required
def profile_form(request):
    # Retrieve the logged-in user
    user = request.user
    
    # Filter the profile queryset based on the logged-in user's email
    try:
        profile = Profile.objects.get(email=user.email)
    except Profile.DoesNotExist:
        profile = None
    
    # Check if the user is authorised to update their profile
    if profile is None:
        return HttpResponseForbidden("You are not authorised to update this profile.")

    if request.method == 'POST':
        # Check if the form is submitted by the same user
        if request.POST.get('email') != user.email:
            return HttpResponseForbidden("You are not authorised to update this profile.")
        
        form = UserForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            # Redirect to profile_form_success URL
            return redirect('profile_form_success')
    else:
        form = UserForm(instance=profile)
    
    return render(request, 'profile_form.html', {'form': form})

# Render view_myaccount if logged-in and retrieve user profile info
@login_required
def view_myaccount(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myaccount') # redirect to myaccount when form saved
    else:
        try:
            profile = Profile.objects.get(email=request.user.email)
            return render(request, 'view_myaccount.html', {'profile': profile})
        except Profile.DoesNotExist:
            # If profile does not exist, present user with profile form, prepopulated with their email
            initial_data = {'email': request.user.email}
            form = UserForm(initial=initial_data)
            return render(request, 'profile_form.html', {'form': form})

# Render profile_form_success if logged in
@login_required
def profile_form_success(request):
    user = request.user
    return render(request, 'profile_form_success.html', {'user': user})
