from multiprocessing import context
from django.shortcuts import render
from .models import Food


def food_list(request):
    foods = Food.objects.all
    context = {
        "foods" : foods
    }
    return render(request,'foods/list.html',context)


def food_detail(request,id):
    food = Food.objects.get(id=id)
    context = {
        "food":food
    }
    return render(request,"foods/detail.html",context)