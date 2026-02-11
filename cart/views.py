from django.shortcuts import render, redirect
from products.models import Product
from .models import CartItem

def cart(request):
    cart_ids = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart_ids)

    total_price = 0
    for product in products:
        total_price += product.price

    return render(request, 'cart.html', {
        'products': products,
        'total_price': total_price
    }) 



def add_to_cart(request, product_id):
    cart = request.session.get('cart', [])

    product_id = int(product_id)

    if product_id not in cart:
        cart.append(product_id)

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')

def remove_from_cart(request, item_id):
    cart = request.session.get('cart', [])

    if item_id in cart:
        cart.remove(item_id)

    request.session['cart'] = cart
    return redirect('cart')
