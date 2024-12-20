from lib2to3.fixes.fix_input import context

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def index(request):
    recipes = DATA.keys()
    response_text = "Доступные рецепты:\n" + "\n".join(recipes)
    return HttpResponse(response_text)


def recipe(request, recipe_name):
    servings = int(request.GET.get('servings', 1))
    recipe_data = DATA.get(recipe_name)

    if recipe_data is None:
        return render(request, 'recipes.html', {'error': "Рецепт не найден."})

    scaled_recipe = {ingredient: amount * servings for ingredient, amount in recipe_data.items()}

    context = {
        'recipe': scaled_recipe,
        'servings': servings,
    }

    return render(request, 'recipes.html', context)