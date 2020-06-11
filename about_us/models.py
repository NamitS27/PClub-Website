from django.db import models

# Create your models here.
class About(models.Model):
    club_description = models.TextField()
    faculty_advisor_fn = models.CharField(max_length=30)
    faculty_advisor_ln = models.CharField(max_length=30)
    faculty_advisor_photo = models.ImageField(default=None,blank=True,upload_to="images/")
    secretary_fn = models.CharField(max_length=30)
    secretary_ln = models.CharField(max_length=30)
    secretary_photo = models.ImageField(default=None,blank=True,upload_to="images/")
    joint_secretary_fn = models.CharField(max_length=30)
    joint_secretary_ln = models.CharField(max_length=30)
    joint_secretary_photo = models.ImageField(default=None,blank=True,upload_to="images/")
    treasurer_fn = models.CharField(max_length=30)
    treasurer_ln = models.CharField(max_length=30)
    treasurer_photo = models.ImageField(default=None,blank=True,upload_to="images/")

class Member(models.Model):
    member_fn = models.CharField(max_length=30)
    member_ln = models.CharField(max_length=30)