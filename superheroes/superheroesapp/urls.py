from . import views
from django.urls import path

app_name = 'superheroesapp'
urlpatterns = [
    path('', views.index, name='index')
]
