from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe, Category
from .forms import RecipeForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect




def home(request):
    recipes = Recipe.objects.order_by('?')[:5]
    categories = Category.objects.all()
    return render(request, 'recipes/home.html', {'recipes': recipes, 'categories': categories})





def category_recipes(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    recipes = category.recipes.all()
    return render(request, 'recipes/category_recipes.html', {'category': category, 'recipes': recipes})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'recipes/signup.html', {'form': form})

def home(request):
    recipes = Recipe.objects.order_by('?')[:5]  # 5 случайных рецептов
    return render(request, 'recipes/home.html', {'recipes': recipes})

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            form.save_m2m()  # Сохраняем многие ко многим
            return redirect('home')
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})

@login_required
def edit_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id, author=request.user)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/edit_recipe.html', {'form': form})





