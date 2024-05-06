from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'pedal_name', 'manufacturer_name', 'category_name', 'price', 'description', 'condition', 'image1', 'image2']
