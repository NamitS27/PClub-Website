from django.db import models

# Create your models here.
class Platform(models.Model):
    platform_name = models.CharField(max_length=200)
    platform_link = models.URLField(max_length=200)

class Contest(models.Model):
    contest_id = models.ForeignKey(Platform,on_delete=models.CASCADE)
    contest_name = models.CharField(max_length=200)
    contest_duration = models.CharField(max_length=100)
    contest_start = models.DateTimeField(blank=True)
    contest_end =   models.DateTimeField(blank=True)
    contest_link = models.URLField(max_length=200)

class Server_time(models.Model):
    server_update_time = models.DateTimeField(null=False)

class PClub_contest(models.Model):
    platform_name = models.CharField(max_length=200)
    contest_name = models.CharField(max_length=200)
    contest_duration = models.CharField(max_length=100)
    contest_start = models.DateTimeField(blank=True)
    contest_end = models.DateTimeField(blank=True)
    contest_link = models.URLField(max_length=100)