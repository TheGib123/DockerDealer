from django.contrib import admin

# Register your models here.

from .models import Car, Truck, Suv, Motorcycle
admin.site.register(Car)
admin.site.register(Truck)
admin.site.register(Suv)
admin.site.register(Motorcycle)
