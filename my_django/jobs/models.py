from django.db import models

from organizations.models import Category, Organizations

# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=[('Full time', 'Full time'), ('Part Time', 'Part Time')])
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    level = models.CharField( max_length=255)
    description = models.TextField()
    requirement =models.TextField()
    experience = models.TextField()
    skills = models.TextField()
    responsibilities = models.TextField()
    no_of_vacancy = models.IntegerField()
    salary = models.FloatField()
    deadline = models.DateField()
    organization = models.ForeignKey(Organizations, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title} - {self.organization}'