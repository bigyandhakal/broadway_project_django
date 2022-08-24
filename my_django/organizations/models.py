
from django.utils import timezone
from django.db import models

from accounts.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField()
    status = models.BooleanField(default= True)

    def __str__(self):
        return self.title

class Organizations(models.Model):
    name = models.CharField(max_length=255)
    estd = models.DateField()
    address = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    details = models.TextField()
    status = models.BooleanField(default=True)
    logo = models.ImageField(upload_to='organizations')

    def __str__(self):
        return self.name


class OrgUser(models.Model):
    org = models.ForeignKey(Organizations, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default = timezone.now())

    