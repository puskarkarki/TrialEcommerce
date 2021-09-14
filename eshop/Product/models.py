from django.db import models

# Create your models here.
from meroshop.models import Category
from django.urls import reverse


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products',  on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, db_index=True)
    brand = models.CharField(max_length=255)
    sku = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    old_price = models.DecimalField(
        max_digits=9, decimal_places=2, default=0.00)
    image = models.ImageField(upload_to='')
    quantity = models.IntegerField(default=0)
    description = models.TextField()
    stock = models.IntegerField()
    meta_keywords = models.CharField(max_length=255)
    meta_description = models.CharField(max_length=255)
    is_available = models.BooleanField(default=False)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name_plural = "Products"
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        
        return reverse('Product:product_detail',
                       args=[self.id, self.slug])
