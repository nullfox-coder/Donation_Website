from django.db import models

# Create your models here.

class Contactform(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.CharField(max_length=100)
    Subject=models.CharField(max_length=200)
    Message=models.TextField()