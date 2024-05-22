from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import uuid
from users.models import Profile
from django_resized import ResizedImageField
from djmoney.models.fields import MoneyField

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.title}"

class Manufacturer(models.Model):
    title = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return f"{self.title}"

class Pedal(models.Model):
    pedal_name = models.CharField(max_length=200, unique=True)
    manufacturer_name = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    catergory_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.pedal_name}"

class Listing(models.Model):
    title = models.CharField(max_length=200, unique=True)
    pedal_name = models.ForeignKey(Pedal, on_delete=models.CASCADE)
    manufacturer_name = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    listing_date = models.DateTimeField(auto_now_add=True)
    price = MoneyField(decimal_places=2, default_currency='GBP', max_digits=6,)
    description = models.TextField()
    CONDITION_CHOICES = [
        ('As_New', 'As New'),
        ('Good', 'Good'),
        ('Well_Used', 'Well Used'),
        ('Broken', 'Broken'),
    ]
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='Good')
    image1 = CloudinaryField('image', blank=True, null=True)
    image2 = CloudinaryField('image', blank=True, null=True)

    class Meta:
        ordering = ["-listing_date"]
    def __str__(self):
        return f"{self.title} - {self.price.amount:.2f} {self.price.currency}"



