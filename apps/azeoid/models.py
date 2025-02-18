from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import random
import string

class AzeoProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    azeo_id = models.CharField(max_length=10, unique=True)
    college = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    year_of_study = models.IntegerField(choices=[
        (1, '1st Year'),
        (2, '2nd Year'),
        (3, '3rd Year'),
        (4, '4th Year'),
        (5, '5th Year'),
    ])
    phone = models.CharField(max_length=15)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.azeo_id} - {self.user.get_full_name()}"

    @staticmethod
    def generate_azeo_id():
        while True:
            # Generate random ID: AZEO followed by 6 digits
            azeo_id = 'AZEO' + ''.join(random.choices(string.digits, k=6))
            if not AzeoProfile.objects.filter(azeo_id=azeo_id).exists():
                return azeo_id

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        AzeoProfile.objects.create(
            user=instance,
            azeo_id=AzeoProfile.generate_azeo_id()
        )