from django.contrib import admin
from .models import *
from django import forms 


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category', 'modified_at', 'is_available',)
    list_display_links = ('name',)
    list_per_page = 20
    prepopulated_fields = {'slug':('name',)}
    search_fields = ['name', 'category']
    exclude = ('created_at', 'updated_at',)
  

admin.site.register(Product, ProductAdmin)





        
        