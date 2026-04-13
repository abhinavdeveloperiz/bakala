from django.contrib import admin
from django.utils.html import format_html
from .models import Banner, Product, Gallery, Testimonial


def image_preview(obj):
    if obj.image:
        return format_html(
            '<img src="{}" style="width:80px;height:80px;object-fit:cover;border-radius:8px;" />',
            obj.image.url
        )
    return "-"
image_preview.short_description = "Preview"


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')
    search_fields = ('title', 'description')
    readonly_fields = ('image_tag',)
    list_per_page = 10

    def image_tag(self, obj):
        return image_preview(obj)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag')
    search_fields = ('name',)
    readonly_fields = ('image_tag',)
    list_per_page = 15

    def image_tag(self, obj):
        return image_preview(obj)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_tag')
    readonly_fields = ('image_tag',)
    list_per_page = 20

    def image_tag(self, obj):
        return image_preview(obj)


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag')
    search_fields = ('name', 'feedback')
    readonly_fields = ('image_tag',)
    list_per_page = 15

    def image_tag(self, obj):
        return image_preview(obj)
