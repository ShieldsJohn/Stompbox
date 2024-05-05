from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import uuid
from users.models import Profile
from django_resized import ResizedImageField

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
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    listing_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    CONDITION_CHOICES = [
        ('As_New', 'As New'),
        ('Good', 'Good'),
        ('Well_Used', 'Well Used'),
        ('Broken', 'Broken'),
    ]
    condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='Good')
    image1 = ResizedImageField(
        force_format='WEBP', quality=75, blank=True,
        upload_to='static/images', default='static/images/image_coming_soon.png')
    image2 = ResizedImageField(
        force_format='WEBP', quality=75, upload_to='static/images', blank=True)

    class Meta:
        ordering = ["-listing_date"]
    def __str__(self):
        return f"{self.title}"



