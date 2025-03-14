from django.db import models

# Create your models here.

class HotelModel(models.Model):
    name = models.CharField(max_length=50, default="Unknow")
    branch_no = models.IntegerField()