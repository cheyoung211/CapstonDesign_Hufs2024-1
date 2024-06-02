from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class homeimport(TemplateView):
    # template_name = 'home.html'
    template_name = 'mybodymap.html'