from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name="upload_file"),
]