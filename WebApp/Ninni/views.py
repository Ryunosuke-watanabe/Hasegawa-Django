from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import *

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class MyListView(ListView):
    template_name = 'list.html'
    model = MyDataBase