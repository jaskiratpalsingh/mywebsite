# Create your models here.
from django.db import models
from django.utils import timezone

class Customer(models.Model):
    user_name = models.CharField(max_length=200)
    first_name=models.CharField;
    last_name=models.CharField;
    email_id= models.CharField(max_length=200)
    phone_number=models.CharField(max_length=10)
    city = models.TextField()
    state = models.TextField()
    country = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    profit=models.IntegerField;

class Product(models.Model):
    product_id=models.CharField(max_length=10);
    brand=models.CharField(max_length=200)
    purchase_date = models.DateTimeField(
        default=timezone.now)
    sell_date = models.DateTimeField(
        default='')
    dealer=models.CharField(max_length=200)
    historic_price=models.IntegerField;
    sell_price=models.IntegerField;
    product_image = models.FileField(default='')
    product_quantity=models.IntegerField;
    expiry_date=models.DateTimeField(default='');
    product_info=models.CharField;

class SoldProduct(models.Model):
    prod_id=models.CharField;
    cus_id=models.CharField;
    date = models.DateTimeField(
        default='')

class OrderedProduct(models.Model):
    prod_id = models.CharField;
    cus_id = models.CharField;
    date = models.DateTimeField(
        default='')




