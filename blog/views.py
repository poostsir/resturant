from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Blog, Category, Tag, Comments
from .forms import CommentsForm
from django.core.paginator import Paginator

def blog_list(request):
    blogs = get_list_or_404(Blog)
    paginator = Paginator(blogs,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "blogs":page_obj
    }
    return render(request,"blog/blog.html",context)

def blog_detail(request,id):
    blog = get_object_or_404(Blog,id=id)
    tags = Tag.objects.all().filter(blogs=blog)
    recents = Blog.objects.all().order_by("-created")[:3]
    categories = Category.objects.all()
    comments = Comments.objects.all().filter(blog=blog)

    if request.method == 'POST':
        comments_form = CommentsForm(request.POST)
        if comments_form.is_valid():
            new_name = comments_form.cleaned_data['name']
            new_email = comments_form.cleaned_data['email']
            new_message = comments_form.cleaned_data['message']
            new_comment = Comments(blog=blog,name=new_name,email=new_email,message=new_message)
            new_comment.save()

    context = {
        "blog":blog ,
        "tags":tags ,
        "recents":recents ,
        "categories":categories ,
        "comments":comments ,
    }
    return render(request,'blog/blog-details.html',context)


def blog_tags(request,tag):
    blogs = Blog.objects.filter(tag__slug=tag)
    context = {
        "blogs":blogs
    }
    return render(request,"blog/blog.html",context)

def blog_categories(request,category):
    blogs = Blog.objects.filter(category__slug=category)
    context = {
        "blogs":blogs
    }
    return render(request,"blog/blog.html",context)

def search(request):
    if request.method == 'GET':
        q = request.GET.get('search')
    blog_list = Blog.objects.filter(title__icontains=q)
    if blog_list.count() == 0:
        blog_list = Blog.objects.filter(content__icontains=q)
    return render(request,"blog/blog.html",{"blogs":blog_list})