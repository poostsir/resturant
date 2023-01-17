from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    published = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title 


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    published = models.DateTimeField(auto_now=False, auto_now_add=True)
    update = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title 

class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    content = RichTextField()
    created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/%Y/%m/%d')
    category = models.ForeignKey(Category,related_name='blog',on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag,related_name='blogs')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Article"

class Comments(models.Model):
    blog = models.ForeignKey(Blog,related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField()
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
            return self.name