from django.contrib import admin
from .models import Contact, Gallery, Book, PortfolioCategory, Portfolio, About, Blog, Category, SlideShow
from django.utils.html import format_html

admin.site.register((Contact, Book, PortfolioCategory, Portfolio, About, Category, SlideShow)) 

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('img','title','category_name')
    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))

    def category_name(self, obj):
        return obj.category.name
    
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'slug')

    def img(self, obj):
        return format_html(
            '<img width="100" height="100" src="{}" style="border-radius: 50%;" />',
            obj.image.url
        )