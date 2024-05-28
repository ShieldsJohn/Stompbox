from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib.auth.models import User
from .forms import ProfileForm
from .models import Profile
from django.contrib.auth import get_user_model, logout
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.urls import reverse_lazy

# Render myaccount page if logged in
@login_required
def myaccount(request):
    return render(request, "myaccount.html")

@login_required
def profile_form(request):
    user = request.user
    try:
        profile = Profile.objects.get(email=user.email)

    except Profile.DoesNotExist:
        profile = None
    
    if profile is None:
        return HttpResponseForbidden("You are not authorised to update this profile.")

    if request.method == 'POST':
        if request.POST.get('email') != user.email:
            return HttpResponseForbidden("You are not authorised to update this profile.")
        
        form = ProfileForm(request.POST, instance=profile)
        
        if form.is_valid():
            form.save()
            return redirect('profile_form_success')
        else:
            print(form.errors)  # Print form errors to console
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'profile_form.html', {'form': form})

@login_required
def view_myaccount(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_form_success')
        else:
            print(form.errors)  # Print form errors to console
    else:
        try:
            profile = Profile.objects.get(email=request.user.email)
            return render(request, 'view_myaccount.html', {'profile': profile})
        except Profile.DoesNotExist:
            initial_data = {'email': request.user.email}
            form = ProfileForm(initial=initial_data)
            return render(request, 'profile_form.html', {'form': form})

    return render(request, 'view_myaccount.html', {'form': form})

# Render profile_form_success if logged in
@login_required
def profile_form_success(request):
    user = request.user
    return render(request, 'profile_form_success.html', {'user': user})

# Delete user and account/profile
@login_required
def delete_account_confirmation(request):
    if request.method == 'POST':
        confirm_delete = request.POST.get('confirm_delete')
        if confirm_delete == 'Yes':
            user = request.user
            try:
                profile = Profile.objects.get(email=user.email)
                profile.delete()
            except Profile.DoesNotExist:
                pass  # If profile doesn't exist/deleted
            
            user.delete()
            logout(request)
            messages.success(request, 'Your MyStompbox has been successfully deleted.')
            return redirect(reverse_lazy('home'))
        elif confirm_delete == 'No':
            messages.info(request, 'MyStompbox deletion cancelled.')
            return redirect('myaccount')  # Redirect back to myaccount page
    return render(request, 'delete_account_confirmation.html')

def account_deleted(request):
    return render(request, 'account_deleted.html')
