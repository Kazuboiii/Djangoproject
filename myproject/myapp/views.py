from django.shortcuts import render,redirect
from .models import Product ,Cart, Customer
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import CustomersignupForm, CustomerloginForm



# Create your views here.
def home(request):
   products = Product.objects.all()[:8]  # Display only the first 8 products
   return render(request, 'home.html', 
   {'products': products})

def about(request): 
   return render(request, 'about.html')

def contact(request):
   return render(request, 'contact.html') 

def shop(request):
   products = Product.objects.all()
   return render(request, 'Shop.html', {'products': products})


@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)  # fetch current user's cart
    cart_total = sum(item.totalprice() for item in cart_items)  # calculate total
    return render(request, 'cart.html', {
        'cart_items': cart_items,
        'cart_total': cart_total
    })


@login_required
def add_to_cart(request, product_id):
   product = Product.objects.get(id=product_id)
   cart_item, created = Cart.objects.get_or_create(user=request.user, products=product)
   if not created:
       cart_item.quantity += 1
       cart_item.save()
   return redirect('cart')

# @login_required
# def remove_from_cart(request, product_id):
#    product = Product.objects.get(id=product_id)
#    cart_item = Cart.objects.filter(user=request.user, products=product).first()
#    if cart_item:
#        cart_item.delete()  
#    return redirect('cart')
@login_required
def remove_from_cart(request, cart_id):
    Cart.objects.filter(id=cart_id, user=request.user).delete()
    return redirect('cart')

def search(request):
   query = request.GET.get('q', '')
   results = Product.objects.filter(name__icontains=query) if query else []
   return render(request, 'search.html', {'products': results, 'query': query})


def customersignup(request):
   if request.method == 'POST':
       form = CustomersignupForm(request.POST)
       if form.is_valid():
           form.save()
           message.success(request, 'Account created successfully')
           return redirect('home')
   else:
       form = CustomersignupForm()
   return render(request, 'customersignup.html', {'form': form})

def customerlogin(request):
   if request.method == 'POST':
       form = CustomerloginForm(request, data=request.POST)
       if form.is_valid():
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password')
           user = authenticate(request, username=username, password=password)
           if user is not None:
               login(request, user)
               return redirect('home')
           else:
              message.error(request, 'Invalid username or password')
   else:
       form = CustomerloginForm()
   return render(request, 'customerlogin.html', {'form': form})

def customerlogout(request):
   logout(request)
   return redirect('home')