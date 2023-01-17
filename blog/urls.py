from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("",views.blog_list,name='bloglist'),
    path("<int:id>",views.blog_detail,name='blogdetail'),
    path("tags/<slug:tag>",views.blog_tags,name='tags'),
    path("categories/<slug:category>",views.blog_categories,name='categories'),
    path("search/",views.search,name='search'),
]
