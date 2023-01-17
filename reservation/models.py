from django.db import models



class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    number = models.PositiveIntegerField()
    day = models.DateField(auto_now=False, auto_now_add=False)
    hour = models.TimeField()

    def __str__(self):
        return self.name