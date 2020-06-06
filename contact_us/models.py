from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=300)
    subject = models.CharField(max_length=200)
    description = models.TextField()
    join_whatsapp = models.BooleanField(default=False)