from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect


# Create your views here.

def safe_asli_site(request):
    products = [
        {'id': 1, 'name': 'Samsung 24 Ultra ', 'price': 1000, 'quantity': 10, 'discount': '5 % '},
        {'id': 2, 'name': 'Iphone 15 pro max ', 'price': 2000, 'quantity': 2, 'discount': '10 % '},
        {'id': 3, 'name': 'Xiaomi 17  ', 'price': 1000, 'quantity': 100, 'discount': '30 % '},
    ]
    return render(request, 'index.html', {'products': products})


def aboutus(request):
    # return ""
    return render(request, "aboutus.html")


def get_post(request, id):
    return ""
    # return render(request, 'post_get.html', {'id': id})
