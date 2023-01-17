from django.shortcuts import render
from foods.models import Food
from gallery.models import Gallery
# Create your views here.

def food_list(request):
    foods = Food.objects.all
    pictures = Gallery.objects.all()
    context = {
        "foods" : foods,
        "pictures" : pictures,
    }
    return render(request,'pages/index.html',context)

def about(request):
    foods = Food.objects.all
    context = {
        "foods" : foods
    }
    return render(request,'pages/about.html',context)

def menu(request):
    foods = Food.objects.all
    context = {
        "foods" : foods
    }
    return render(request,'pages/menu.html',context)

def stuff(request):
    return render(request,'pages/stuff.html',context=None)