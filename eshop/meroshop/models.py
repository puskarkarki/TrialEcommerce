from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    meta_keywords = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    class Meta:

        db_table = 'categories'
        verbose_name = 'category'
        ordering = ('name',)
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('meroshop:product_list_by_category',
               args=[self.slug])
