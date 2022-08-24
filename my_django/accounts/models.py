from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
# Create your models here.

class User(AbstractUser):
    mobile = models.CharField(max_length=20, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    role = models.CharField(max_length=20, choices=[('Employer','Employer'),
                                                    ('Recuriter','Recuriter'),
                                                    ('Employee','Employee')], default='Employer')