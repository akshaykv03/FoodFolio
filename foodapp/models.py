from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    usertype=models.CharField(max_length=20,null=True)

class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    goal=models.CharField(max_length=100)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)

class Supplier(models.Model):
    comapny_name=models.CharField(max_length=50)
    owner_name=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)

class Delivery(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    status=models.CharField(max_length=20,default="Available")
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)


class Food(models.Model):
    goal=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    desc=models.CharField(max_length=303)
    incredients=models.CharField(max_length=303)
    nutrients=models.CharField(max_length=303)
    time=models.CharField(max_length=303)
    amount=models.CharField(max_length=303)
    price=models.IntegerField()
    image=models.FileField(null=True)
    status=models.CharField(max_length=20,null=True,default="Request Pending")
    user=models.ForeignKey(Supplier,on_delete=models.CASCADE)

class Bookings(models.Model):
    cust=models.ForeignKey(User,on_delete=models.CASCADE)  
    food=models.ForeignKey(Food,on_delete=models.CASCADE)   
    boy=models.ForeignKey(Delivery,on_delete=models.CASCADE,null=True)   
    status=models.CharField(max_length=50,default="CART")
    count=models.IntegerField(default=1)
    cart_date=models.DateTimeField(auto_now_add=True)
    book_date=models.DateTimeField(null=True)
    payment_date=models.DateTimeField(null=True)
    total=models.IntegerField()
    boy=models.ForeignKey(Delivery,on_delete=models.CASCADE,null=True)

class Feedback(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    book=models.ForeignKey(Bookings,on_delete=models.CASCADE)
    review=models.CharField(max_length=300)
    rating=models.IntegerField()

class Guidence(models.Model):
    date=models.DateTimeField(auto_now_add=True)
    goal=models.CharField(max_length=30)
    shop=models.ForeignKey(Supplier,on_delete=models.CASCADE)
    file=models.FileField(null=True)