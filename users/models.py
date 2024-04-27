from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    first_name = models.CharField(max_length=200, unique=True)
    surname = models.SlugField(max_length=200, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    city = models.CharField(max_length=200, unique=True)
    country = models.CharField(max_length=200, unique=True)
    # profile_img = models.ImageField(upload_to='users/', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
