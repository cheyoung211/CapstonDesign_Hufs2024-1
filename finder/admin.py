from django.contrib import admin
from .models import Disease, TranslatedDisease

# Register your models here.

admin.site.register(Disease)
admin.site.register(TranslatedDisease)