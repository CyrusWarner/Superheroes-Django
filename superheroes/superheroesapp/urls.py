from . import views
from django.urls import path

app_name = 'superheroesapp'
urlpatterns = [
    path('', views.index, name='index'),
    # path('<int:superhero_id>/', views.superhero_detail, name='detail'),
    path('new/', views.create_new_superhero, name='create_new_superhero')
]
