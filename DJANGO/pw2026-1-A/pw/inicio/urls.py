from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('dsf/', views.dsf, name='dsf'),
    path('adb/', views.adb, name='adb'),
    path('gr/', views.gr, name='gr'),
    path('ia/', views.ia, name='ia'),
    path('agregar/', views.agregar_servicio, name='agregar_servicio'),
    path('eliminar/', views.eliminar_servicio, name='eliminar_servicio'),
    path('servicio/<slug:slug>/', views.servicio_dinamico, name='servicio_dinamico'),
]