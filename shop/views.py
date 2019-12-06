from django.shortcuts import render

# Create your views here.

from .models import Product


def index(request):
    return render(request, 'home/home.html')


def contact(request):
    return render(request, 'contact/contact.html')


def shop(request):
    return render(request, 'shop/shop.html')


def about(request):
    return render(request, 'about/about.html')


def product(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product/products.html', context)

