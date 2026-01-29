from django.shortcuts import render
from .models import Product

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

def cart(request):
   return render(request, 'cart.html')

def search(request):
   query = request.GET.get('q', '')
   results = Product.objects.filter(name__icontains=query) if query else []
   return render(request, 'search.html', {'products': results, 'query': query})