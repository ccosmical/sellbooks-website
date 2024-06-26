from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField(max_length=25, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
