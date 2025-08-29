from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderCreateForm
from .models import Order, OrderItem
from apps.cart.cart import Cart

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid() and len(cart) > 0:
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product_name=item['name'], price=item['price'], quantity=item['quantity'])
            cart.clear()
            return redirect('orders:success', order_id=order.id)
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html', {'cart': cart, 'form': form})

def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/success.html', {'order': order})
