# from datetime import datetime
from django.db import models
from django.utils import timezone
from jobs.models import Job
from accounts.models import User

# Create your models here.

class Application(models.Model):
    apply_date = models.DateField(default=timezone.now())
    # js = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, choices=[('Applied', 'Applied'), ('Review', 'Review'), ('Selected', 'Selected'),('Rejected', 'Rejected'),('Waiting', 'Waiting')]) 


    def __str__(self):
        return f'{ self.user } - { self.job }'
 