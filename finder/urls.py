from django.contrib import admin
from django.urls import path
from . import views

app_name = "finder"

urlpatterns = [
    path('', views.testimport.as_view(), name="test")
]