from django.db import models

class Platform(models.Model):
    platform_name = models.CharField(max_length=200)
    platform_link = models.URLField(max_length=200)

    def __str__(self):
        return self.platform_name

class Contest(models.Model):
    contest_id = models.ForeignKey(Platform,on_delete=models.CASCADE)
    contest_name = models.CharField(max_length=200)
    contest_duration = models.CharField(max_length=100)
    contest_start = models.DateTimeField(blank=True)
    contest_end =   models.DateTimeField(blank=True)
    contest_link = models.URLField(max_length=200)

    def __str__(self):
        return self.contest_name
class Server_time(models.Model):
    server_update_time = models.DateTimeField(null=False)

    def __str__(self):
        return str(self.server_update_time)
class PClub_contest(models.Model):
    platform_name = models.CharField(max_length=200)
    contest_name = models.CharField(max_length=200)
    contest_duration = models.CharField(max_length=100)
    contest_start = models.DateTimeField(blank=True)
    contest_end = models.DateTimeField(blank=True)
    contest_link = models.URLField(max_length=100)

    def __str__(self):
        return self.contest_name