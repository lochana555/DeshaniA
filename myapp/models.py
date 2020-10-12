from django.db import models


class Products(models.Model):
    pid=models.CharField(max_length=10)
    pname=models.CharField(max_length=255)
    price=models.FloatField()
    stock=models.IntegerField()

