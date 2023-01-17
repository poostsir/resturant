from django.db import models
from django.contrib.auth.models import User

class Cantact(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    email = models.EmailField()
    person = models.PositiveIntegerField()
    message = models.TextField()

    def __str__(self):
        return self.name