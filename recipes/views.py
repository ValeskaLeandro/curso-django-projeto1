from django.http import HttpResponse
from django.shortcuts import render
from utils.recipes.factory import make_recipe

from recipes.models import Recipe


# Create your views here.
def home(request):
    # Ordenando por ordem de cadastro invertida
    recipes = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    # Ordenando por ordem de cadastro invertida
    recipes = Recipe.objects.filter(category_id=category_id).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
