from django import forms
from .models import Listing 

# Listing form
class ListingForm(forms.ModelForm):
    price = forms.DecimalField(
        decimal_places=2,
        max_digits=6,
        widget=forms.NumberInput(attrs={'step': '0.01'}))

    class Meta:
        model = Listing
        fields = ['title', 'pedal_name', 'manufacturer_name', 'category_name', 'price', 'description', 'condition', 'image1', 'image2']

    def clean_price(self):
        price = self.cleaned_data['price']
        return round(price, 2)

        
