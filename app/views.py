from django.shortcuts import render
from app.models import Product,Banner,gallery

# Create your views here.

def home(request):
    banner=Banner.objects.last()
    context={
        'banner':banner,
    }
    return render(request, 'home.html',context)

def about(request):
    return render(request, 'about.html')

def products(request):
    return render(request, 'products.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')