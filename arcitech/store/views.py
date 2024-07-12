from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        if request.method=='GET':
            products= Product.objects.all()
            cart = Cart.objects.get(user=request.user)
            item_count = cart.item_count()
            context={
                'products': products,
                'count':item_count

            }
            return render(request, 'home.html', context=context)
        if request.method=='POST':
            #add to cart
            pass
    else:
        return render(request, 'login.html')

def category(request, cat):
    if request.user.is_authenticated:
        if request.method=='GET':
            products= Product.objects.filter(category=cat)
            cart = Cart.objects.get(user=request.user)
            item_count = cart.item_count()
            context={
                'products': products,
                'count':item_count

            }
            return render(request, 'home.html', context=context)
    else:
        return render(request, 'login.html')
    

def search(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            q= request.POST['q']
            products= Product.objects.filter(name__contains=q)
            cart = Cart.objects.get(user=request.user)
            item_count = cart.item_count()
            context={
                'products': products,
                'count':item_count

            }
            return render(request, 'home.html', context=context)
    else:
        return render(request, 'login.html')
    
def cart(request):
    if request.user.is_authenticated:
        cart= Cart.objects.get(user=request.user)
        item= CartItem.objects.filter(cart=cart.id)
        context={
            "items":item
        }
        return render(request, 'cart.html', context=context)
    else:
        return render(request, 'login.html')

  
def addToCart(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            product_id= request.POST['id']
            product_obj= Product.objects.get(id=product_id)
            cart, created= Cart.objects.get_or_create(user=request.user)
            cart_item, created =CartItem.objects.get_or_create(cart=cart, product=product_obj)
            if not created:
                cart_item.quantity += 1
                cart_item.save()
            else:
                cart_item.save()
                
            return redirect('home')
        return render(request, 'cart.html')
    else:
        return render(request, 'login.html')


def checkout(request):
    if request.user.is_authenticated:
        return render(request, 'checkout.html')
    else:
        return render(request, 'login.html')


def orders(request):
    if request.user.is_authenticated:
        return render(request, 'orders.html')
    else:
        return render(request, 'login.html')