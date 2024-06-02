from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib.auth.models import User
from .forms import ProfileForm, ContactForm
from .models import Profile
from listings.models import Listing
from django.contrib.auth import get_user_model, logout
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.http import HttpResponseRedirect


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

def contact_seller(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender_email = form.cleaned_data['email']
            recipient_email = listing.profile.user.email
            send_mail(subject, message, sender_email, [recipient_email])
            # Redirect to home page with a confirmation message
            messages.success(request, 'Your message has been sent successfully.')
            return redirect('home')
    else:
        form = ContactForm()

    return render(request, 'contact_seller.html', {'form': form, 'listing': listing})