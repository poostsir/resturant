from django.shortcuts import render
from .forms import ReservationForm
from django.contrib import messages

def reservation(request):
    reservation_form = ReservationForm()
    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation_form.save()
            messages.add_message(request,messages.SUCCESS,'Your table is booked!!')
    else:
        reservation_form = ReservationForm()
    context = {
        "form":reservation_form
    }
    return render(request,'reservation/reservation.html',context)

