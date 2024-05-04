from django.contrib import admin
from django.urls import path
from . import views

app_name = "finder"

urlpatterns = [
    path('', views.finderimport.as_view(), name="finder"),
    path('head/', views.HeadImport.as_view(), name="head"),
    path('upperbody/', views.UpperBodyImport.as_view(), name="upperbody"),
    path('belly/', views.BellyImport.as_view(), name="belly"),
    path('pelvis/', views.PelvisImport.as_view(), name="Pelvis"),
    path('arm/', views.ArmImport.as_view(), name="arm"),
    path('arm/onlyarm/', views.OnlyArmImport.as_view(), name="onlyarm"),
    path('arm/hand/', views.HandImport.as_view(), name="hand"),
    path('leg/', views.LegImport.as_view(), name="leg"),
    path('leg/onlyleg/', views.OnlyLegImport.as_view(), name="onlyleg"),
    path('leg/foot/', views.FootImport.as_view(), name="foot"),
]