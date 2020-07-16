from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    type=models.CharField(max_length=5)

class article(models.Model):
    name=models.CharField(max_length=30)
    category=models.CharField(max_length=30)
    authorname=models.CharField(max_length=30)
    content=models.CharField(max_length=60500)

class operation(models.Model):
    email=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    time=models.CharField(max_length=50)
    job=models.CharField(max_length=10)