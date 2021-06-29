from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Superhero

# Create your views here.


def index(request):

    all_superheroes = Superhero.objects.all()
    context = {
        'all_superheroes': all_superheroes
    }

    return render(request, 'superheroesapp/index.html', context)



def superhero_detail(request):
    pass


def create_new_superhero(request):
    if request.method == 'POST':
        superhero_name = request.POST.get('name')
        superhero_alter_ego = request.POST.get('alter_ego')
        superhero_primary_ability = request.POST.get('primary_superhero_ability')
        superhero_secondary_ability = request.POST.get('secondary_superhero_ability')
        superhero_catchphrase = request.POST.get('superhero_catchphrase')
        new_superhero = Superhero(superhero_name=superhero_name, alter_ego_name=superhero_alter_ego, primary_hero_ability=superhero_primary_ability, secondary_hero_ability=superhero_secondary_ability, superhero_catchphrase=superhero_catchphrase)
        new_superhero.save()

        return HttpResponseRedirect(reverse('superheroesapp:index'))
    else:
        return render(request, 'superheroesapp/index.html')


def edit(request):
    pass


def delete_superhero(request):
    pass
