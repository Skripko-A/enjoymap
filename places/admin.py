from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin, SortableTabularInline, SortableAdminBase

from .models import Location, Image


@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['file', 'get_preview']
    readonly_fields = ['get_preview']

    def get_preview(self, img):
        return format_html('<img src="{}" style="max-width:300px; max-height:200px"/>'.format(img.file.url))


class ImageTabularInline(SortableTabularInline):
    readonly_fields = ['get_preview']
    fields = ['position', ('file', 'get_preview')]
    model = Image

    def get_preview(self, img):
        return format_html('<img src="{}" style="max-width:300px; max-height:200px"/>'.format(img.file.url))


@admin.register(Location)
class LocationAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ImageTabularInline, ]
    search_fields = ['title', ]
