from django.conf import Settings, settings
from django.urls import path


from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('orders', views.orders, name='orders'),
]