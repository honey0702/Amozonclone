from django.shortcuts import render, get_object_or_404
from .models import Product
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    query = request.GET.get('q')

    if query:
        

      products = Product.objects.filter(name__icontains=query)

      if not products:
             products = Product.objects.filter(
             Q(description__icontains=query) |
             Q(category__icontains=query)
    )
        
    else:
        products=  Product.objects.all()
    cart = request.session.get('cart' ,{})
    cart_count = sum(cart.values())

    return render(request , 'home.html', {
        'products' : products,
        'query' : query,
        'cart_count' : cart_count
    })

    



def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html' , {'product': product})

def add_to_cart(request,id):
    cart = request.session.get('cart' , {})

    if str(id) in cart:
        cart[str(id)] += 1
    else:
        cart[str(id)] = 1
    request.session['cart'] = cart
    return redirect('/shop/')

def cart(request):
    cart = request.session.get('cart' , {})
    products = []
    total = 0

    for key, value in cart.items():
        product = Product.objects.get(id=int(key))
        product.qty = value
        product.total = product.price * value
        total += product.total
        products.append(product)

    return render(request , 'cart.html' , {'products' : products, 'total' : total} )

def update_cart(request,id,action):
    cart =  request.session.get('cart' , {})

    if str(id) in cart:
        if action == 'increase':
            cart[str(id)] += 1
        
        elif action == 'decrease':
            cart[str(id)] -= 1
            if cart[str(id)] <= 0 :
                del cart[str(id)]
            
        elif action == 'remove':
            del cart[str(id)]
    
    request.session['cart'] = cart
    return redirect('/cart/')


def category(request,name):
    products = Product.objects.filter(category__iexact=name)
    return render(request,'home.html' ,{'products' : products})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html' , {'error' : 'Invalid credentials'})
    return render(request , 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')