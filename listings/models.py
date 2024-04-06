from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()

class Manufacturer(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)   

class Pedal(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    manufacturer_name = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    catergory_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()

class Listing(models.Model):
    pedal_name = models.ForeignKey(Pedal, on_delete=models.CASCADE)
    manufacturer_name = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    catergory_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    # seller_name = models.ForeignKey(MyAccount, on_delete=models.CASCADE) #MyAccount not yet created
    listing_date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()
    condition = models.CharField(max_length=200, unique=True)
   #add listing images here ref Cloudinary lesson

