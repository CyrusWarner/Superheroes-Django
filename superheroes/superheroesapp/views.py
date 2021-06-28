from django.shortcuts import render
from .models import Superhero
# Create your views here.


def index(request):
    return render(request, 'superheroesapp/index.html')


def create_new_superhero(request):
    pass


def edit(request):
    pass


def delete(request):
    pass
