from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('',views.food_list,name="home"),
    path('about/',views.about,name="about"),
    path('menu/',views.menu,name="menu"),
    path('stuff/',views.stuff,name="stuff"),
    
]