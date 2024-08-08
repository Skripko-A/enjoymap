from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Location, Image


# Register your models here.


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['filename', 'get_preview']
    readonly_fields = ['get_preview']
    fields = ['filename', 'get_preview', 'position']

    def get_preview(self, obj):
        return format_html('<img src="{}" style="max-width:300px; max-height:200px"/>'.format(obj.filename.url))


class ImageInline(admin.TabularInline):
    readonly_fields = ['get_preview']
    model = Image

    def get_preview(self, obj):
        return format_html('<img src="{}" style="max-width:300px; max-height:200px"/>'.format(obj.filename.url))


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ImageInline, ]
