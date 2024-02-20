from django.shortcuts import render

from products.models import Product, Category


# Create your views here.

def index(request):
    context = {
        'title': 'Store',
        'isDiscount': False
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store',
        'isDiscount': True,
        'products': Product.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'products/products.html', context)
