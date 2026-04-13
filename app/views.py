from django.shortcuts import render
from django.core.cache import cache
from app.models import Product, Banner, Gallery, Testimonial


def home(request):
    data = cache.get("home_data")

    if not data:
        data = {
            "banner": Banner.objects.only("title", "description", "image").last(),
            "test": Testimonial.objects.only("name", "feedback", "image"),
            "products": Product.objects.only("name", "image").order_by("-id")[:10],
        }
        cache.set("home_data", data, 60 * 5) 

    return render(request, "home.html", data)


def products(request):
    products = cache.get("products_data")

    if not products:
        products = Product.objects.only("name", "image").order_by("-id")
        cache.set("products_data", products, 60 * 10)

    return render(request, "products.html", {"products": products})


def gallery(request):
    gallery = cache.get("gallery_data")

    if not gallery:
        gallery = Gallery.objects.only("image").order_by("-id")
        cache.set("gallery_data", gallery, 60 * 10)

    return render(request, "gallery.html", {"gallery": gallery})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")