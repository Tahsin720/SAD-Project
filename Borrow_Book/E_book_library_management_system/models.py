from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="profile_pic/default.png", upload_to = "profile_pic/")
    mobile_num = models.IntegerField(null = True, blank = True)
    location = models.CharField(null = True, blank = True, max_length=40)
    balance = models.IntegerField(default = 0)
    def __str__(self):
        return self.user.username

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
    cost=models.IntegerField(default=0)
    time = models.DateTimeField()
    def __str__(self):
        return self.name

class my_request(models.Model):
    reqId = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=20)
    requester = models.CharField(max_length=20)
    accepted = models.CharField(default="Processing", max_length=10)
    time = models.DateTimeField()
    deliveryManId = models.IntegerField(default=0)
    def __str__(self):
        return self.requester
    
class my_request_log(models.Model):
    requester = models.CharField(max_length=20)
    isbn = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)
    date_time = models.DateTimeField()
    def __str__(self):
        return self.requester

class Review_for_books(models.Model):
    Id = models.AutoField(primary_key=True)
    posted_by = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    text = models.TextField(max_length=200)
    date_time = models.DateTimeField()
    def __str__(self):
        return self.posted_by

class book_log(models.Model):
    isbn = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    user_name = models.CharField(max_length=20)
    date_time = models.DateTimeField()
    def __str__(self):
        return self.name

class Report(models.Model):
    id = models.IntegerField(primary_key=True)
    posted_by = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    text = models.TextField(max_length=200)
    reporter = models.CharField(max_length=20)
    date_time = models.DateTimeField()
    def __str__(self):
        return self.posted_by

class payment(models.Model):
    paid_by = models.CharField(max_length=20)
    account_num = models.CharField(max_length=20)
    amount = models.CharField(max_length=20)
    payment_method = models.TextField(max_length=200)
    date_time = models.DateTimeField()
    def __str__(self):
        return self.paid_by
