from django.shortcuts import render
from .models import Superhero
# Create your views here.


def index(request):
    return render(request, 'superheroesapp/index.html')
