from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    def __str__(self):
        return f"{self.title}"

class Manufacturer(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)   
    def __str__(self):
        return f"{self.title}"

class Pedal(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    manufacturer_name = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    catergory_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    def __str__(self):
        return f"{self.title}"

class Listing(models.Model):
    title = models.CharField(max_length=200, unique=True)
    pedal_name = models.ForeignKey(Pedal, on_delete=models.CASCADE)
    manufacturer_name = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    # seller_name = models.ForeignKey(MyAccount, on_delete=models.CASCADE) #MyAccount not yet created
    listing_date = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()
    CONDITION_CHOICES = [
        ('As_New', 'As New'),
        ('Good', 'Good'),
        ('Well_Used', 'Well Used'),
        ('Broken', 'Broken'),
    ]
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='Good')
   #add listing images here ref Cloudinary lesson
    class Meta:
        ordering = ["-listing_date"]
    def __str__(self):
        return f"{self.title}"


