from django.contrib import admin
from .models import Location, Image


# Register your models here.


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('filename',)


class ImageInline(admin.TabularInline):
    model = Image


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ImageInline, ]
