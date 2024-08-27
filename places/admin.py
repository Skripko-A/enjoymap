from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminMixin, SortableTabularInline, SortableAdminBase

from .models import Location, Image


IMAGE_PREVIEW_WIDTH = '300px'
IMAGE_PREVIEW_HEIGHT = '200px'

@admin.register(Image)
class ImageAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['file', 'get_preview']
    readonly_fields = ['get_preview']
    autocomplete_fields = ['location']

    def get_preview(self, img):
        return format_html(
            '<img src="{}" style="max-width:{}; max-height:{}"/>',
            img.file.url,
            IMAGE_PREVIEW_WIDTH,
            IMAGE_PREVIEW_HEIGHT
        )

class ImageTabularInline(SortableTabularInline):
    readonly_fields = ['get_preview']
    fields = ['position', ('file', 'get_preview')]
    model = Image

    def get_preview(self, img):
        return format_html(
            '<img src="{}" style="max-width:{}; max-height:{}"/>',
            img.file.url,
            IMAGE_PREVIEW_WIDTH,
            IMAGE_PREVIEW_HEIGHT
        )


@admin.register(Location)
class LocationAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ImageTabularInline, ]
    search_fields = ['title', ]
