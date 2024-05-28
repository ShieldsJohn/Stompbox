from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Listing
from users.models import Profile
from .forms import ListingForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()

@login_required
def my_listings(request):
    context = {}  # Initialize the context dictionary
    
    try:
        # Attempt to get the user's profile
        profile = request.user.profile
        # If profile exists, get the user's listings
        listings = Listing.objects.filter(profile=profile)
        context['listings'] = listings
    except ObjectDoesNotExist:
        # If the profile doesn't exist, handle the error
        profile = None
        # Set listings to an empty queryset
        context['listings'] = Listing.objects.none()

    return render(request, "my_listings.html", context)
    
# Render create listing page if logged-in
@login_required
def create_listing(request):
    try:
        logged_in_user = request.user
        profile = get_object_or_404(Profile, email=logged_in_user.email)
        missing_fields = []
        if not profile.first_name:
            missing_fields.append('first name')
        if not profile.surname:
            missing_fields.append('surname')
        if not profile.email:
            missing_fields.append('email address')
        if missing_fields:
            missing_fields_str = ', '.join(missing_fields)
            messages.error(request, f'Please complete your profile. Missing fields: {missing_fields_str}.')
            print("Redirecting to profile_form due to missing fields.")
            return redirect('profile_form')
    except Profile.DoesNotExist:
        print("Profile does not exist for user:", request.user.username)
        messages.error(request, "Please create your profile before creating a listing.")
        print("Redirecting to profile_form due to profile does not exist.")
        return redirect('profile_form')

    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.price_currency = 'GBP'
            form.instance.profile = profile
            try:
                form.save()
                print("Listing created successfully. Redirecting to my_listings.")
                return redirect('my_listings')
            except Exception as e:
                print("Error saving listing:", e)
                messages.error(request, 'Failed to create listing.')
        else:
            print(form.errors)
    else:
        initial_currency = {'price_currency': 'GBP'}
        form = ListingForm(initial=initial_currency)

    return render(request, 'create_listing.html', {'form': form})

# Render listing detail page if logged in
@login_required
def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, 'listing_detail.html', {'listing': listing})

# Render update listing page if logged in
@login_required
def update_listing(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listing_detail', pk=listing.pk)
    else:
        initial_data = {'price': listing.price.amount}
        form = ListingForm(instance=listing, initial=initial_data)
        print("Form initial data:", form.initial)
        print("Listing price:", form.initial)
    return render(request, 'update_listing.html', {'form': form, 'listing': listing})

# Render delete listing page if logged-in
@login_required
def delete_listing(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    if request.method == 'POST':
        if request.POST.get('confirm_delete') == 'Yes':
            listing.delete()
            messages.success(request, 'Listing deleted successfully!')
        else:
            messages.info(request, 'Listing deletion cancelled.')
        return redirect('my_listings')
    return render(request, 'delete_listing.html', {'listing': listing})