"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import include


from core.views import home, orders, reviews, category, register
from products.views import product_list, detail
from cart.views import cart, add_to_cart, remove_from_cart
from django.conf import settings
from django.conf.urls.static import static
from core.views import order, order_success

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    path('home/', home, name='home'),

    path('products/', product_list, name='products'),
    path('products/<int:id>/', detail, name='detail'),

    path('cart/', cart, name='cart'),
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),


    path('order/', order, name='order'),
    path('order/success/', order_success, name='order_success'),
    path('order/', include('orders.urls')),


    path('orders/', orders, name='orders'),
    path('reviews/', reviews, name='reviews'),
    path('category/<str:name>/', category, name='category'),
    path('order/success/', order_success, name='order_success'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)