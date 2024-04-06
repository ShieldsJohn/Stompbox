from django.contrib import admin
from .models import Category, Pedal, Manufacturer, Listing

# Register your models here.
admin.site.register(Category)
admin.site.register(Pedal)
admin.site.register(Manufacturer)
admin.site.register(Listing)
