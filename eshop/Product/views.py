from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import AddProductToCartForm

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(is_available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})
    
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, is_available=True)
    add_product_form = AddProductToCartForm() 
    return render(request, 'detail.html', {'product':product, 'add_product_form':add_product_form})
    

    
