from django.contrib import admin
from blog.models import Blog, Category, Comments, Tag

@admin.register(Blog)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','title','description','author','created',]
    search_fields = ['title','content']
    date_hierarchy = 'created'
    list_filter = ['created','category','tag']


@admin.register(Category)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['title','published']

@admin.register(Tag)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['title','published','update']

@admin.register(Comments)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name','email','date','message','blog']