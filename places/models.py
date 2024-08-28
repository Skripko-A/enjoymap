from django.db import models
from tinymce.models import HTMLField


class Location(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название', unique=True)
    short_description = models.TextField(blank=True, verbose_name='Краткое описание')
    long_description = HTMLField(blank=True, verbose_name='Подробное описание')
    lng = models.DecimalField(max_digits=18, decimal_places=14, verbose_name='Долгота')
    lat = models.DecimalField(max_digits=18, decimal_places=14, verbose_name='Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    file = models.ImageField(upload_to='places/images', verbose_name='Картинка')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='images', verbose_name='Локация')
    position = models.PositiveIntegerField(verbose_name='Позиция', blank=True, default=0, db_index=True)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f'self.file'
