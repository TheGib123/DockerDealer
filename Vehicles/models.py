from django.db import models
import os
# Create your models here.


class Car(models.Model):
    year = models.CharField(max_length=4)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.IntegerField()
    kind = models.Value("Car")
    description = models.CharField(max_length=200)
    pic = models.ImageField(upload_to='gallery', null=False)
    pic1 = models.ImageField(upload_to='gallery', default="none", null=True)
    pic2 = models.ImageField(upload_to='gallery', default="none", null=True)
    pic3 = models.ImageField(upload_to='gallery', default="none", null=True)
    pic4 = models.ImageField(upload_to='gallery', default="none", null=True)

    def __str__(self):
        title = self.year + " " + self.make + " " + self.model
        return title

class Truck(models.Model):
    year = models.CharField(max_length=4)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.IntegerField()
    kind = models.Value("Truck")
    description = models.CharField(max_length=200)
    pic = models.ImageField(upload_to='gallery', blank=True, null=True)

    def __str__(self):
        title = self.year + " " + self.make + " " + self.model
        return title

class Suv(models.Model):
    year = models.CharField(max_length=4)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.IntegerField()
    kind = models.Value("Suv")
    description = models.CharField(max_length=200)
    pic = models.ImageField(upload_to='gallery', blank=True, null=True)

    def __str__(self):
        title = self.year + " " + self.make + " " + self.model
        return title

class Motorcycle(models.Model):
    year = models.CharField(max_length=4)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.IntegerField()
    kind = models.Value("Motorcycle")
    description = models.CharField(max_length=200)
    pic = models.ImageField(upload_to='gallery', blank=True, null=True)

    def __str__(self):
        title = self.year + " " + self.make + " " + self.model
        return title