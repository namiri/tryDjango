from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def home_view (request, *args, **kwargs):
    item= Product.objects.get(id=1)
    return render(request, "home.html")
    # return HTTPResponse("<h1>Hello </h1>")