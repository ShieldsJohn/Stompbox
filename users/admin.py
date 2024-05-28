from django.contrib import admin
from .models import Profile
from .forms import ProfileForm

# Register your models here

class Profile_Admin(admin.ModelAdmin):
    form = ProfileForm

admin.site.register(Profile, Profile_Admin)
