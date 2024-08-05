from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=255, default='')
    image = models.ImageField(upload_to='places/images')

    def __str__(self):
        return f'{self.title}'


class Location(models.Model):
    title = models.CharField(max_length=100, default='')
    image = models.ManyToManyField(Image, null=True, blank=True, related_name='images')
    description_short = models.TextField(null=True, blank=True)
    description_long = models.TextField(null=True, blank=True)
    lng = models.DecimalField(max_digits=17, decimal_places=14, default=37.6155600)
    lat = models.DecimalField(max_digits=17, decimal_places=14, default=55.7522200)

    def __str__(self):
        return f'{self.title}'



