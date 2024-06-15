from django.shortcuts import render
from django.views import generic
from django.shortcuts import redirect
from listings.models import Category


def home(request):
    # Retrieve all categories from the database
    categories = Category.objects.all()
    return render(request, "home_page/home.html", {"categories": categories})


def socials(request, platform):
    platform_urls = {
        'facebook': 'https://facebook.com',
        'twitter': 'https://twitter.com',
        'instagram': 'https://www.instagram.com',
        'youtube': 'https://www.youtube.com',
    }
    # use the platform parameter to redirect to relevant URL
    if platform in platform_urls:
        return redirect(platform_urls[platform])
    else:
        return redirect('home')
