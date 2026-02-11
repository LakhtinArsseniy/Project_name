from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Order


@login_required
def create_order(request):
    cart_ids = request.session.get('cart', [])

    if not cart_ids:
        return redirect('cart')

    products = Product.objects.filter(id__in=cart_ids)

    total = sum(product.price for product in products)

    # 🔥 ОЦЕ ГОЛОВНЕ
    order = Order.objects.create(
        user=request.user,
        total_price=total
    )

    order.products.set(products)

    # очищаємо кошик
    request.session['cart'] = []

    return redirect('order_success', order_id=order.id)


@login_required
def order_success(request, order_id):
    order = Order.objects.get(id=order_id)

    return render(request, 'orders/success.html', {
        'order': order
    })
