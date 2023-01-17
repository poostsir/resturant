from django.urls import path
from . import views

app_name = 'cantact'

urlpatterns = [
    path("",views.cantact,name='cantact')
]
