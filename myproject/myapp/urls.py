from .import views
from django.urls import path

urlpatterns = [
   
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    #cart
    path('cart/', views.cart_view, name='cart'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:cart_id>/', views.remove_from_cart, name='remove_from_cart'),

    path('signup/', views.customersignup, name='signup'),
    path('login/', views.customerlogin, name='login'),
    path('logout/', views.customerlogout, name='logout'),

    path('search/', views.search, name='search'),
]