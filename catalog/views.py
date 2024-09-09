from itertools import product
from lib2to3.fixes.fix_input import context

from django.shortcuts import render, get_object_or_404

from .models import Product


def index_list(request):
    product = Product.objects.all()
    context = {'product' : product}

    return render(request, 'product_list.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    #product = Product.objects.get(pk=pk)
    context = {'product' : product}

    return render(request, 'product_detail.html', context)
