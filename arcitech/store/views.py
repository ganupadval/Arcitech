from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    if request.user.is_authenticated:
        if request.method=='GET':
            products= Product.objects.all()
            context={
                'products': products,

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
            context={
                'products': products,
            }
            return render(request, 'home.html', context=context)
    else:
        return render(request, 'login.html')
    

def search(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            q= request.POST['q']
            products= Product.objects.filter(name__contains=q)
            context={
                'products': products,
            }
            return render(request, 'home.html', context=context)
    else:
        return render(request, 'login.html')
    
def cart(request):
    if request.user.is_authenticated:
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