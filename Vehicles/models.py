from django.db import models
import os
# Create your models here.


class Vehicle(models.Model):
    year = models.CharField(max_length=4)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    pic = models.ImageField(upload_to='gallery', null=False)
    pic1 = models.ImageField(upload_to='gallery', default="none", null=True)
    pic2 = models.ImageField(upload_to='gallery', default="none", null=True)
    pic3 = models.ImageField(upload_to='gallery', default="none", null=True)
    pic4 = models.ImageField(upload_to='gallery', default="none", null=True)

    def __str__(self):
        title = self.year + " " + self.make + " " + self.model
        return title

    def all_pic_urls(self):
        all_fields = Car._meta.fields
        pics = []
        for field in all_fields:
            if ("pic" in field.name and field.name != "pic"):
                picVal = getattr(self, field.name)
                if (picVal != "none"):
                    pics.append(getattr(getattr(self, str(field.name)), "url"))
        return pics

    def count_pics(self):
        all_fields = Car._meta.fields
        list_count = []
        pic_count = 0
        for field in all_fields:
            if ("pic" in field.name and field.name != "pic"):
                picVal = getattr(self, field.name)
                if (picVal != "none"):
                    pic_count = pic_count + 1
                    list_count.append(pic_count)
        return list_count

    class Meta:
        abstract = True

class Car(Vehicle):
  pass

class Truck(Vehicle):
  pass

class Suv(Vehicle):
  pass

class Motorcycle(Vehicle):
  pass
