from itertools import product
from lib2to3.fixes.fix_input import context

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import PermissionsMixin
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from .models import Product



#@login_required
#@permission_required('catalog.view_product')
#def index(request):
#    product_list = Product.objects.all()
#    context = {
#        'object_list': product_list,
#        'title': 'Главная',
#    }
#    return render(request, 'catalog/index.html', context)
#
#
#@login_required
#def





class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    fields = ('name', 'description', 'category', 'image', 'price')
    permission_required = ('catalog.change_product',)
    success_url = reverse_lazy('catalog:product_list')

    def get_queryset(self):
        # Ограничиваем доступ только к продуктам текущего пользователя
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)


class ProductDeLeteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    permission_required = ('catalog.delete_product',)
    success_url = reverse_lazy('catalog:product_list')



class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    fields = ('name', 'description', 'category', 'image', 'price')
    permission_required = ('catalog.add_product',)
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Устанавливаем владельца
        return super().form_valid(form)






