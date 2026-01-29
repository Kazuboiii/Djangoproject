from .import views
from django.urls import path

urlpatterns = [
   
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    #cart
    path('cart/', views.cart, name='cart'),


    path('search/', views.search, name='search'),
]