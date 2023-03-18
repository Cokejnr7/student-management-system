from django.db import models

# Create your models here.

class Student(models.Model):
    pass


class Biodata(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    # title = models.CharField(max_length=,choices=)