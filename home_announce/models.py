from django.db import models
from datetime import date

class Announcement(models.Model):
    announcement_title = models.CharField(max_length=200)
    announcement_date = models.DateTimeField(auto_now_add=True)
    announcement_description = models.TextField(max_length=730)
    announcement_isofEvent = models.BooleanField(default=False)
    announcement_isActive = models.BooleanField(default=True)

    def __str__(self):
        return self.announcement_title

class Daily(models.Model):
    question = models.CharField(max_length=250)
    answer = models.CharField(max_length=150,blank=True,null=True)
    question_isQuote = models.BooleanField(default=False)
    question_tobeadded = models.DateField()

    def __str__(self):
        return str(self.question_tobeadded)
    



            