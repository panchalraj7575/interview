from django.db import models
from django.db.models.fields import AutoField

# Create your models here.


class customer(models.Model):
    c_id = AutoField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    contactNo = models.IntegerField()
    pincode = models.IntegerField()

    def __str__(self):
        return self.firstName


class product(models.Model):
    p_id = AutoField(primary_key=True)
    productName = models.CharField(max_length=50)
    productPrice = models.IntegerField()

    def __str__(self):
        return self.productName


class CutomerOreder(models.Model):
    co_id = AutoField(primary_key=True)
    productPrice = models.IntegerField()
    Qty = models.IntegerField()
    TotalPrice = models.IntegerField()
    customer_id = models.ForeignKey(customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(product, on_delete=models.CASCADE)

    def __str__(self):
        return self.productName
