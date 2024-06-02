from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class aiimport(TemplateView):
    template_name = 'AI_app.html'
