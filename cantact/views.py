from django.shortcuts import render
from .forms import CantactForm
from django.contrib import messages
from .models import Cantact


def cantact(request):
    cantact_form = CantactForm()
    if request.method == 'POST':
        cantact_form = CantactForm(request.POST)
        if cantact_form.is_valid():
            new_name = cantact_form.cleaned_data['name']
            new_email = cantact_form.cleaned_data['email']
            new_message = cantact_form.cleaned_data['message']
            new_person = cantact_form.cleaned_data['person']
            new_cantact = Cantact(user=request.user,name=new_name,email=new_email,message=new_message,person=new_person)
            new_cantact.save()
            messages.add_message(request,messages.SUCCESS,'Your message is send!')
    else:
        cantact_form = CantactForm()
    context = {
        "form":cantact_form
    }
    return render(request,'cantact/cantact.html',context)