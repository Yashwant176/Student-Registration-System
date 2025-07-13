from django.db import models

# Create your models here.
class Details(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    city=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    standard=models.IntegerField()
    af=models.IntegerField()
    pa=models.IntegerField()
    balance=models.IntegerField()

