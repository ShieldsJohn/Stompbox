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
    print("my_listings view called")
    context = {} #initialise the context dictionary
    if request.user.is_authenticated:
        try:
             # Get logged-in user
            logged_in_user=request.user
            # Get user profile
            profile=get_object_or_404(Profile, email=logged_in_user.email)
            listings = Listing.objects.filter(profile=profile)

            for listing in listings:
                print(f"Listing PK: {listing.pk}")

        except ObjectDoesNotExist:
            print(f"Profile does not exist for user {request.user}")
            # If the profile doesn't exist, handle the error
            profile = None
            listings = Listing.objects.none()

        context['listings'] = listings
        context['messages'] = messages.get_messages(request) # Pass messages to template context
        
        return render(request, "my_listings.html", context)
    else:
        # If user not logged-in, redirect to login page
        return redirect('login')
    

# Render create listing page if logged-in
@login_required
def create_listing(request):
    try:
        # Get logged-in user
        logged_in_user=request.user
        # Get user profile
        profile=get_object_or_404(Profile, email=logged_in_user.email)
        # Set missing fields to empty string
        missing_fields = []
        # Check what's missing
        if not profile.first_name:
            missing_fields.append('first name')
        if not profile.surname:
            missing_fields.append('surname')
        if not profile.email:
            missing_fields.append('email address')
        # If any fields are missing, return an error message
        if missing_fields:
            missing_fields_str=', '.join(missing_fields)
            messages.error(request, f'Please complete your profile.  Missing fields: {missing_fields_str}.')
            return redirect('profile_form')

    except Profile.DoesNotExist:
        print("Profile does not exist for user:", request.user.username)
        messages.error(request, "Please create your profile before creating a listing.")
        return redirect('profile_form')

    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.price_currency = 'GBP'
            form.instance.profile = profile  # Associate the listing with the user's profile

            try:
                form.save()  # Save the listing
                # messages.success(request, 'Listing created successfully!')
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
