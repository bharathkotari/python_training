#update this in model.py
from django.db import models

# Create your models here.
class EmailModel(models.Model):
    emailid = models.CharField(max_length=200)
    emailsubject = models.TextField()
    emailbody = models.CharField(max_length=200)
