from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from products.models import Product


from products.models import Product

import requests

TELEGRAM_TOKEN = "8553170140:AAEdhQNNueurWd1A1xBwC7DFQJa2ftlH_fU"
CHAT_ID = "458458677"

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{8553170140:AAEdhQNNueurWd1A1xBwC7DFQJa2ftlH_fU}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    requests.post(url, data=data)

User = get_user_model()

# 📦 ЗАМОВЛЕННЯ
@login_required
def orders(request):
    return render(request, 'orders.html')


# ⭐ ВІДГУКИ
@login_required
def reviews(request):
    return render(request, 'reviews.html')


# 🗂 КАТЕГОРІЯ
@login_required
def category(request, name):
    return render(request, 'category.html', {'category': name})


# 🛒 КОШИК
@login_required
def cart(request):
    cart_ids = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart_ids)
    return render(request, 'cart.html', {'products': products})


# ➕ ДОДАТИ В КОШИК
@login_required
def add_to_cart(request, product_id):
    cart = request.session.get('cart', [])

    if product_id not in cart:
        cart.append(product_id)

    request.session['cart'] = cart
    return redirect('cart')


def register(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if not username or not password1 or not password2:
            messages.error(request, "Заповніть усі поля")
            return redirect('register')

        if password1 != password2:
            messages.error(request, "Паролі не співпадають")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Користувач уже існує")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            password=password1
        )

        
        login(request, user)

        return redirect('home')

    return render(request, 'register.html')



def home(request):
    if not request.user.is_authenticated:
        return redirect('login')

    products = Product.objects.all()[:6]  
    return render(request, 'home.html', {
        'products': products
    })

@login_required
def order(request):
    if request.method == "POST":
        # очищаємо кошик
        request.session['cart'] = []
        return redirect('order_success')

    return render(request, 'order.html')


@login_required
def order_success(request):
    return render(request, 'order_success.html')

