from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction
from django.db.utils import IntegrityError
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    first_name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.first_name} {self.surname}"
    # Code below provided by Tomas Kubancik at Code Institute
    # Receiver added to automatically create profile    
    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        """
        Create or update the user profile class signal receiver
        """
        if created:
            # Check if profile with the same email already exists
            try:
                with transaction.atomic():
                    if not Profile.objects.filter(email=instance.email).exists():
                        Profile.objects.create(user=instance, email=instance.email)
                    else:
                        print(f"A profile with email {instance.email} already exists.")
            except IntegrityError:
                print(f"An error occurred while creating the profile for email {instance.email}.")
        else:
            # Update profile if the user instance is updated
            try:
                profile = Profile.objects.get(user=instance)
                profile.save()
            except Profile.DoesNotExist:
                # Handle the case where the profile does not exist
                print(f"Profile for user {instance.username} does not exist.")