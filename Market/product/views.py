from itertools import product
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import product_model



def x(request):
    products = product_model.objects.all()
    return(
     render(request,"x.html",{"products":products}))
    