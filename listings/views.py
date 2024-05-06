from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Listing
from .forms import ListingForm

# Render my_listings page if logged in
@login_required
def my_listings(request):
    return render(request, "my_listings.html")

# Render create listing page if logged in
@login_required
def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.user = request.user.profile  # Assumes user profile is associated with the listing
            listing.save()
            return redirect('listing_detail', pk=listing.pk)
    else:
        form = ListingForm()
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
            return redirect('listing_detail', pk=pk)
    else:
        form = ListingForm(instance=listing)
    return render(request, 'update_listing.html', {'form': form})

# Redner delete listing page if logged in
@login_required
def delete_listing(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    if request.method == 'POST':
        listing.delete()
        return redirect('my_listings')  # Redirect to my_listings
    return render(request, 'delete_listing.html', {'listing': listing})
