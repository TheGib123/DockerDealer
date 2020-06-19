from django.shortcuts import render

# Create your views here.

from .models import Car, Motorcycle, Suv, Truck
#from Vehicles.models import Car, Motorcycle, Suv, Truck


def index(request):
    context = {}
    return render(request, 'Vehicles/home.html', context)

def car_post(request, v_id):
    vehicle = Car.objects.get(pk=v_id)
    context = {'vehicle' : vehicle}
    return render(request, 'Vehicles/post.html', context)

def truck_post(request, v_id):
    vehicle = Truck.objects.get(pk=v_id)
    context = {'vehicle' : vehicle}
    return render(request, 'Vehicles/post.html', context)

def suv_post(request, v_id):
    vehicle = Suv.objects.get(pk=v_id)
    context = {'vehicle' : vehicle}
    return render(request, 'Vehicles/post.html', context)

def motorcycle_post(request, v_id):
    vehicle = Motorcycle.objects.get(pk=v_id)
    context = {'vehicle' : vehicle}
    return render(request, 'Vehicles/post.html', context)




def motorcycle(request):
    vehicle_list = Motorcycle.objects.all()
    context = {'vehicle_list' : vehicle_list}
    return render(request, 'Vehicles/postings.html', context)

def car(request):
    vehicle_list = Car.objects.all()
    context = {'vehicle_list' : vehicle_list}
    return render(request, 'Vehicles/postings.html', context)

def truck(request):
    vehicle_list = Truck.objects.all()
    context = {'vehicle_list' : vehicle_list}
    return render(request, 'Vehicles/postings.html', context)

def suv(request):
    vehicle_list = Suv.objects.all()
    context = {'vehicle_list' : vehicle_list}
    return render(request, 'Vehicles/postings.html', context)
