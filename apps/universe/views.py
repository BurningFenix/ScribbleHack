#from django.shortcuts import render
from django.views.generic import ListView
from .models import World, Writing

# Create your views here.
class Universe(ListView):
	model = World

class WritingList(ListView):
	model = Writing