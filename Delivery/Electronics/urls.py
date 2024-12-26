
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.store,name="store"),
    path('cart/',views.cart,name="cart"),
    path('check/',views.check,name="check"),
    path('home/',views.main,name="home"),
    path('main/',views.home,name="main"),
    path('add/',views.add,name="add"),
    path('contact/',views.contact,name="contact"),
    path('product/',views.product,name="product"),
    path('cart/', views.cart, name='cart'),
    path('mobile/<int:pk>/',views.detail_mobile,name="mobile"),
    path('earphone/<int:pk>/',views.detail_earphone,name="earphone"),

    path('charger/<int:pk>/',views.detail_charger,name="charger"),

    path('detail/<int:pk>/',views.detail_PC,name="detail"),
]

