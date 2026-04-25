from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('dsf/', views.dsf, name='dsf'),
    path('adb/', views.adb, name='adb'),
    path('gr/', views.gr, name='gr'),
]