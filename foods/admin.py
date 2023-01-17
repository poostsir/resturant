from django.contrib import admin
from .models import Food


@admin.register(Food)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name','type_food']