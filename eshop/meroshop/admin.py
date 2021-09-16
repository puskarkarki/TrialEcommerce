from django.contrib import admin
from .models import Category

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    # sets up values for how admin site lists categories
    list_display = ('name', 'slug', 'created_at', 'updated_at',)
    ordering = ['name']
    prepopulated_fields = {'slug': ('name',)}

