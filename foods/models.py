from django.db import models

# Create your models here.


class Food(models.Model):
    FOOD_TYPE=[
        ("drinks","نوشیدنی"),
        ("lunch","نهار"),
        ("dinner","شام"),
    ]
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    rate = models.IntegerField(default=0)
    price = models.IntegerField()
    time = models.IntegerField()
    pub_date = models.DateField(auto_now=False,auto_now_add =True)
    photo = models.ImageField(upload_to='foods/%Y/%m/%d',blank=True)
    type_food = models.CharField(max_length=20,choices=FOOD_TYPE,default="drinks")

    def __str__(self):
        return self.name