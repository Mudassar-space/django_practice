from django.db import models

# Create your models here.


class Student(models.Model):
    student_id= models.CharField(max_length=10, default="1001")
    name = models.CharField(max_length=50, default="Unknown")
    branch = models.CharField(max_length=20, default="CS")

    def __str__(self):
        return self.name