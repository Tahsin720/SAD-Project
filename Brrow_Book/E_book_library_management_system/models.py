from django.db import models

class book(models.Model):
    isbn = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    image = models.ImageField(null = True, blank = True, upload_to = "uploads/")
    description = models.TextField(max_length=200)
    user_name = models.CharField(max_length=20)
    isdonated = models.CharField(default="No", max_length=3)
    cost=models.IntegerField
    time = models.TimeField

class request(models.Model):

