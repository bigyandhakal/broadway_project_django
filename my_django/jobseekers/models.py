from django.db import models
from accounts.models import User

# Create your models here.

class Jobseeker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objective = models.TextField(blank=True, null=True)
    qualification = models.TextField(blank=True, null=True)
    training = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    cv = models.FileField(upload_to='cvs')
    image = models.ImageField(upload_to = 'jobseekers')
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

'''
class Qualification(models.Model):
    js = models.ForeignKey(Jobseeker, on_delete=models.CASCADE)
    level = ''
    year = ''
    grade = ''
    board = ''


class Training(models.Model):
    js = models.ForeignKey(Jobseeker, on_delete=models.CASCADE)
    title = ''
    date_from = ''
    date_to= ''
    duration = ''
    remarks = ''
    details = ''



class Experience(models.Model):
    js = models.ForeignKey(Jobseeker, on_delete=models.CASCADE)
    post = ''
    organization = ''
    date_from = ''
    date_to= ''
    duration = ''
    remarks = ''
    responsibilities = ''
    details = ''


class Reference(models.Model):
    js = models.ForeignKey(Jobseeker, on_delete=models.CASCADE)
    name = ''
    post = ''
    organization = ''
    phone = ''
    email = ''
'''