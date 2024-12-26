from django.shortcuts import render
from .models import Charger, Laptop,Mobile,Earphone
# Create your views here.
def store(request):
    context={}
    return render(request,'store.html',context)
def cart(request):
    context={}
    return render(request,'cart.html',context)
def check(request):
    context={}
    return render(request,'check.html',context)

def home(request):
    context={}
    return render(request,'base.html',context)
def add(request):
    context={}
    return render(request,'add.html',context)
def contact(request):
    context={}
    return render(request,'contact.html',context)
def cart(request):
    """Renders the home page with all products."""
    prod = Laptop.objects.all()
    context = {
        'prod': prod,
    }
    return render(request, 'home.html', context)
def product(request):
    products = Laptop.objects.all()
    mobile = Mobile.objects.all()
    earphone =Earphone.objects.all()
    charger =Earphone.objects.all()
    return render(request, 'product.html', {'products': products,'mobile':mobile,'earphone':earphone,'charger':charger})





def detail_PC(request,pk):
    product = Laptop.objects.get(Number=pk)
    return render(request, 'detail.html', {'product': product})
def detail_mobile(request,pk):
    mobile =Mobile.objects.get(Number=pk)
    return render(request, 'mobile.html',{'mobile':mobile})
def detail_earphone(request,pk):
    earphone = Earphone.objects.get(Number=pk)
    return render(request, 'earphone.html',{'earphone':earphone})
def detail_charger(request,pk):
    charger =Charger.objects.get(Number=pk)
    return render(request, 'charger.html',{'charger':charger})
def main(request):
    products = Laptop.objects.all()
    mobiles = Mobile.objects.all()
    earphones =Earphone.objects.all()
    chargers =Charger.objects.all()
    return render(request, 'main.html', {'products': products,'mobiles':mobiles,'earphones':earphones,'chargers':chargers})

