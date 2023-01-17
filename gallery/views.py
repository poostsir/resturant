from multiprocessing import context
from django.shortcuts import render
from .models import Gallery

def pictures(request):
    pictures = Gallery.objects.all()
    context = {
        "pictures" : pictures
    }
    return render(request,"gallery/gallery.html",context)