from django.db import models

# Create your models here.

class appointment(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    subject = models.CharField(max_length=20)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class regis(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11)
    location = models.CharField(max_length=20)
    day = models.CharField(max_length=30)
    month = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)


    def __str__(self):
        return self.first_name
