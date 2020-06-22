from django.db import models
from datetime import date

# Create your models here.
class Announcement(models.Model):
    announcement_title = models.CharField(max_length=200)
    announcement_date = models.DateTimeField(auto_now_add=True)
    announcement_description = models.TextField(max_length=730)
    announcement_image = models.ImageField(default="/static/images/announcement-dafault.png",blank=True,upload_to="images/")
    announcement_isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.announcement_title

class Daily(models.Model):
    question = models.CharField(max_length=250)
    answer = models.CharField(max_length=150)
    question_isQuote = models.BooleanField(default=False)
    question_tobeadded = models.DateField()
    



            