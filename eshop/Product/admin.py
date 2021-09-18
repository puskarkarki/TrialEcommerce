from django.contrib import admin
from .models import *
from django import forms 


# Register your models here.

from django.contrib import admin
from .models import Category

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    # sets up values for how admin site lists categories
    list_display = ('name', 'slug', 'created_at', 'updated_at',)
    ordering = ['name']
    prepopulated_fields = {'slug': ('name',)}


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category', 'modified_at', 'is_available',)
    list_display_links = ('name',)
    list_per_page = 20
    prepopulated_fields = {'slug':('name',)}
    search_fields = ['name', 'category']
    exclude = ('created_at', 'updated_at',)
  

admin.site.register(Product, ProductAdmin)





        
        