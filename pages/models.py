from django.db import models

# Create your models here.

class Trainee(models.Model):
    name = models.CharField(max_length=100)
    cohort = models.CharField(max_length=50)
    credly = models.CharField(max_length=300)

