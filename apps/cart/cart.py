from decimal import Decimal
from django.conf import settings
from apps.catalog.models import Product

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product_id, quantity=1, override=False):
        product = Product.objects.get(id=product_id)
        pid = str(product.id)
        if pid not in self.cart:
            self.cart[pid] = {'quantity': 0, 'price': str(product.price), 'name': product.name}
        self.cart[pid]['quantity'] = quantity if override else self.cart[pid]['quantity'] + quantity
        self.save()

    def remove(self, product_id):
        pid = str(product_id)
        if pid in self.cart:
            del self.cart[pid]
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            item = self.cart[str(product.id)]
            item['product'] = product
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(i['price']) * i['quantity'] for i in self.cart.values())

    def clear(self):
        self.session[settings.CART_SESSION_ID] = {}
        self.save()

    def save(self):
        self.session.modified = True
