# models.py
from django.db import models

class Resource(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.ManyToManyField('Tag')

class Tag(models.Model):
    name = models.CharField(max_length=50)
