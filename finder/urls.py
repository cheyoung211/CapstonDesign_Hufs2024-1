from django.contrib import admin
from django.urls import path
from . import views

app_name = "finder"

urlpatterns = [
    path('', views.finderimport.as_view(), name="finder"),
    path('map/', views.Mapimport.as_view(), name="map"),
    path('headupper/', views.HeadUpperImport.as_view(), name="headupper"),
    path('headupper/head/', views.HeadImport.as_view(), name="head"),
    path('headupper/upperbody/', views.UpperBodyImport.as_view(), name="upperbody"),
    path('bellypelvis/', views.BellyPelvisImport.as_view(), name="bellypelvis"),
    path('bellypelvis/belly/', views.BellyImport.as_view(), name="belly"),
    path('bellypelvis/pelvis/', views.PelvisImport.as_view(), name="Pelvis"),
    path('arm/', views.ArmImport.as_view(), name="arm"),
    path('arm/onlyarm/', views.OnlyArmImport.as_view(), name="onlyarm"),
    # path('arm/hand/', views.HandImport.as_view(), name="hand"),
    path('leg/', views.LegImport.as_view(), name="leg"),
    path('leg/onlyleg/', views.OnlyLegImport.as_view(), name="onlyleg"),
    # path('leg/foot/', views.FootImport.as_view(), name="foot"),
    #이하 찾는 부분
    path('headuppersearch/', views.HeadUpperSearch.as_view(), name='headuppersearch'),
    path('headsearch/', views.HeadSearch.as_view(), name='headsearch'),
    path('upperbodysearch/', views.UpperBodySearch.as_view(), name='upperbodysearch'),
    path('headuppersearch/head/', views.HeadSearch.as_view(), name='headsearch'),
    path('headuppersearch/upperbody/', views.UpperBodySearch.as_view(), name='upperbodysearch'),
    path('bellypelvissearch/', views.BellyPelvisSearch.as_view(), name='bellypelvissearch'),
    path('bellysearch/', views.BellySearch.as_view(), name='bellysearch'),
    path('pelvissearch/', views.PelvisSearch.as_view(), name='pelvissearch'),
    path('bellypelvissearch/belly/', views.BellySearch.as_view(), name='bellysearch'),
    path('bellypelvissearch/pelvis/', views.PelvisSearch.as_view(), name='pelvissearch'),
    path('onlyarmsearch/', views.OnlyArmSearch.as_view(), name='onlyarmsearch'),
    # path('handsearch/', views.HandSearch.as_view(), name='handsearch'),
    path('onlylegsearch/', views.OnlyLegSearch.as_view(), name='onlylegsearch'),
    # path('footsearch/', views.FootSearch.as_view(), name='footsearch'),
]