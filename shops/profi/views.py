
from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator


def product_list(request):
    
    max_price = request.POST.get('price')
    
    # фильтр
    if max_price:
        try:
            max_price = float(max_price)
            products = Product.objects.filter(price__lte=max_price)
        except:
            products = Product.objects.all()
    else:
        products = Product.objects.all()
    
    return render(
        request,
        'profi/product_list.html',
        {'products': products}
    )
