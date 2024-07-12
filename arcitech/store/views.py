from django.shortcuts import render

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
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