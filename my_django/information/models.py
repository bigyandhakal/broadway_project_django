from turtle import title
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Section (models.Model):
    title = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Information(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    details = RichTextUploadingField()
    status = models.BooleanField(default='True')

    def __str__(self):
        return self.title

