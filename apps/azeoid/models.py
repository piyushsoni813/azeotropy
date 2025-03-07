# azeoid/models.py
from django.db import models

class StudentRegistration(models.Model):
    azeoid = models.CharField(max_length=20, unique=True, editable=False)
    name = models.CharField(max_length=100)
    college_name = models.CharField(max_length=200)
    year_of_study = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.azeoid} - {self.name}"