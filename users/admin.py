from django.contrib import admin
from .models import Profile
from .forms import UserForm

# Register your models here

class Profile_Admin(admin.ModelAdmin):
    form = UserForm

admin.site.register(Profile, Profile_Admin)
