from django.db import models

class Gallery(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='gallery/%Y/%m/%d')

    class Meta:
        verbose_name = 'picture'
        verbose_name_plural = 'gallery'

    def __str__(self):
        return self.name
