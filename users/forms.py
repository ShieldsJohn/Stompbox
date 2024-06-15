from django import forms
from django.contrib.auth.models import User
from .models import Profile


# User profile form
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'surname', 'email', 'city', 'country']


# Contact seller form
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
