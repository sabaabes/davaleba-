from django.shortcuts import render
from .models import Product, Category

def product_list(request):
    products = Product.objects.all().order_by('price')
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'store/product_list.html', context)