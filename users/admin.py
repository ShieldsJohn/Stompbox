from django.contrib import admin
from .models import Profile


# Register your models here
@admin.register(Profile)
class Profile_Admin(admin.ModelAdmin):
    #   form = UserForm
    #   admin.site.register(Profile, Profile_Admin)
    list_display = ('surname', 'first_name', 'user', 'email')
