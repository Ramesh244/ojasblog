from django.db import models

# Create your models here.
class Bhagavan(models.Model):
    heading = models.CharField(max_length=100)
    paragram = models.CharField(max_length=200)


class ContactForm(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    feedback=models.CharField(max_length=100)