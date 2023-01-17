from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name','email','number','day','hour']