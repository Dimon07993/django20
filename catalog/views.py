from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from .models import Product

class ProductListView(ListView):
    model = Product



class ProductDetailView(DetailView):
    model = Product



class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description','category','image', 'price')
    success_url = reverse_lazy('catalog:product_list')


class ProductDeLeteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')



#def index_list(request):
#    products = Product.objects.all()
#    context = {'products': products}
#    return render(request, 'catalog/product_list.html', context)

#def product_detail(request, pk):
#    product = get_object_or_404(Product, pk=pk)
#    context = {'item': product}
#    return render(request, 'catalog/product_detail.html', context)


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description','category','image', 'price')
    success_url = reverse_lazy('catalog:product_list')





#from itertools import product
#from lib2to3.fixes.fix_input import context
#
#from django.shortcuts import render, get_object_or_404
#
#from .models import Product
#
#
#def index_list(request):
#    product = Product.objects.all()
#    context = {'product' : product}
#
#    return render(request, 'product_list.html', context)
#
#
#def product_detail(request, pk):
#    product = get_object_or_404(Product, pk=pk)
#    #product = Product.objects.get(pk=pk)
#    context = {'product' : product}
#
#    return render(request, 'product_detail.html', context)
#