from django.db import models

# Create your models here.
class Resource(models.Model):
    resource_topic = models.CharField(max_length=200)
    # resource_description = models.CharField(max_length=2000)

    def __str__(self):
        return self.resource_topic

class Resource_link(models.Model):
    resource_link_id = models.ForeignKey(Resource,on_delete=models.CASCADE)
    resource_link = models.URLField(max_length = 1000)
    resource_link_type = models.CharField(max_length = 50)

    def __str__(self):
        return str(self.resource_link_id)
