from django.contrib import admin
from cantact.models import Cantact

@admin.register(Cantact)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','email','created',]
    search_fields = ['user','name']
    date_hierarchy = 'created'
    list_filter = ['created',]
    ordering = ["-created"]