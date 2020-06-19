from django.urls import path, re_path

from . import views


urlpatterns = [
    re_path(r'^$',views.index, name='index'),
    re_path(r'Cars/(?P<v_id>\d+)/?$', views.car_post),
    re_path(r'Trucks/(?P<v_id>\d+)/?$', views.truck_post),
    re_path(r'Motorcycles/(?P<v_id>\d+)/?$', views.motorcycle_post),
    re_path(r'Suvs/(?P<v_id>\d+)/?$', views.suv_post),
    re_path(r'Motorcycles/', views.motorcycle, name='motorcycles'),
    re_path(r'Cars/', views.car, name='cars'),
    re_path(r'Trucks/', views.truck, name='trucks'),
    re_path(r'Suvs/', views.suv, name='Suvs'),
]
