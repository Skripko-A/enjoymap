from django.db import models
from tinymce.models import HTMLField


class Location(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description_short = models.TextField(null=True, blank=True, verbose_name='Краткое описание')
    description_long = HTMLField(null=True, blank=True, verbose_name='Подробное описание')
    lng = models.DecimalField(max_digits=18, decimal_places=14, default=37.6155600, verbose_name='Долгота')
    lat = models.DecimalField(max_digits=18, decimal_places=14, default=55.7522200, verbose_name='Широта')

    def __str__(self):
        return f'{self.title}'


class Image(models.Model):
    file = models.ImageField(upload_to='places/images', verbose_name='Картинка', null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, related_name='images', null=True)
    position = models.PositiveIntegerField(verbose_name='Позиция', null=True, blank=True, default=0, db_index=True)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f'{self.file}'
