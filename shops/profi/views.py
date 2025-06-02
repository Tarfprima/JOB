
from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.decorators import login_required

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



def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticated(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/profile/')  
        else:
            return render(request, 'profi/login.html', )
    
    return render(request, 'profi/login.html')   



def profile(request):
    if not request.user.is_authenticated:
        return redirect('/login/')
    return render(request, 'profi/profile.html')


