from django.contrib import admin
from django.urls import path
from . import views

app_name = "finder"

urlpatterns = [
    path('', views.finderimport.as_view(), name="finder"),
    path('map/', views.Mapimport.as_view(), name="map"),
    path('head/', views.HeadImport.as_view(), name="head"),
    path('upperbody/', views.UpperBodyImport.as_view(), name="upperbody"),
    path('belly/', views.BellyImport.as_view(), name="belly"),
    path('pelvis/', views.PelvisImport.as_view(), name="Pelvis"),
    path('arm/', views.ArmImport.as_view(), name="arm"),
    path('leg/', views.LegImport.as_view(), name="leg"),
    #이하 찾는 부분
    path('headsearch/', views.HeadSearch.as_view(), name='headsearch'),
    path('upperbodysearch/', views.UpperBodySearch.as_view(), name='upperbodysearch'),
    path('bellysearch/', views.BellySearch.as_view(), name='bellysearch'),
    path('pelvissearch/', views.PelvisSearch.as_view(), name='pelvissearch'),
    path('armsearch/', views.ArmSearch.as_view(), name='armsearch'),
    path('legsearch/', views.LegSearch.as_view(), name='legsearch'),
]