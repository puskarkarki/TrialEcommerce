from decimal import Decimal
from django.conf import settings
from Product.models import Product


class Cart(object):

    def __init__(self, request):
        """
        Initialize the cart with request object and store the current session

        """

        self.session = request.session
        """get cart from the current session"""
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        """
        Add a product to the cart or update it quantity
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product.id] = {
                'quantity': 0, 'price': str(product.price)}
        if override_quantity:
            self.cart[product_id]['quantity'] = [quantity]
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        """
        mark the session as modified to make sure that it is saved
        """
        self.session.modified = True

    """ method for removing the carts from the product """

    def remove(self, product):
        """
        remove product from the cart

        """
        product_id = str(product.id)

        if product_id in self.cart:

            del self.cart[product_id]

            self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products from the database
        """
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id_in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
            
    def __len__(self):
        """
        count all the items in the cart
        """
        return sum(item['quantity'] for item in self.cart.values())
    
    def _get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    
    def clear(self):
        # remove the cart from the session
        
        del self.session[settings.CART_SESSION_ID]
        self.save()
