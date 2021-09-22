from django.shortcuts import render, get_object_or_404, redirect
from Product.models import Product
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import AddProductToCartForm
from cart.forms import AddProductToCartForm

"""
using post decorator to allow only post request
"""
@require_POST 
def cart_add_product(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    """
    We retirive the product instance via product_id and validate AddProductToCartForm
    """
    form = AddProductToCartForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],override_quantity=cd['override'])
        
    return redirect('cart:cart_detail')

@require_POST
def cart_remove_product(request, product_id):
    cart= Cart(request)
    product=get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = AddProductToCartForm(initial={'quantity': item['quantity'],
                                                                   'override': True})
    return render(request, 'cart.html', {'cart': cart})
    
