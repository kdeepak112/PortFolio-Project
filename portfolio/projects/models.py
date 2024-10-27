from django.db import models

# Create your models here.

class projectMaster(models.Model):
    projectId = models.CharField(max_length=50,primary_key=True)
    projectTitle = models.CharField(max_length=250)
    projectDomain = models.CharField(max_length=100)
    projectDescription = models.TextField()
    projectImage = models.ImageField(null=True)