from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from .forms import ProductForm, VersionForm
from .models import Product, Version


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    # fields = ('name', 'description','category','image', 'price')
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST,instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class ProductDeLeteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    # fields = ('name', 'description','category','image', 'price')
    success_url = reverse_lazy('catalog:product_list')



# from itertools import product
# from lib2to3.fixes.fix_input import context
#
# from django.shortcuts import render, get_object_or_404
#
# from .models import Product
#
#
# def index_list(request):
#    product = Product.objects.all()
#    context = {'product' : product}
#
#    return render(request, 'product_list.html', context)
#
#
# def product_detail(request, pk):
#    product = get_object_or_404(Product, pk=pk)
#    #product = Product.objects.get(pk=pk)
#    context = {'product' : product}
#
#    return render(request, 'product_detail.html', context)
#
