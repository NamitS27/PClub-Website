from django.db import models
from datetime import *
# from ckeditor.fields import RichTextField

# Create your models here.

class Events(models.Model):
    name = models.CharField(max_length=200,null=False)
    description = models.TextField()
    logo = models.ImageField(default=None,blank=True,upload_to="images/")
    date = models.DateTimeField(default=None)
    can_register = models.BooleanField(default=False, blank=True)
    feedback_link = models.URLField(max_length=200,blank=True,default=None)
    photos_link = models.URLField(max_length=200,blank=True)
    registration_date = models.DateTimeField(default=None,blank=True)
    registration_link = models.URLField(max_length=200,blank=True) 

    def __str__(self):
        return self.name + ' ' + self.date.strftime('%Y-%m-%d')
