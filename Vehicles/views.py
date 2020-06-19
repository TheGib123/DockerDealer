from django.shortcuts import render

# Create your views here.

from .models import Car, Motorcycle, Suv, Truck
#from Vehicles.models import Car

#### get pictures

def GetCarPics(vehicle):
    all_fields = Car._meta.fields
    print(all_fields[0].name)
    print(getattr(vehicle, str(all_fields[7].name)))

    x = []
    for i in all_fields:
        if ("pic" in i.name):
            picVal = getattr(vehicle, i.name)
            if (picVal != "none"):
                x.append(getattr(getattr(vehicle, str(i.name)), "url"))
    return x

#######################

def index(request):
    context = {}
    return render(request, 'Vehicles/home.html', context)

def car_post(request, v_id):
    vehicle = Car.objects.get(pk=v_id)
    vehiclePics = GetCarPics(vehicle)
    context = {'vehicle' : vehicle, 'vehiclePics' : vehiclePics}
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
