
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.forms import inlineformset_factory

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .models import Product
from .forms import OwnerProductForm, ModeratorProductForm
from .forms import ProductForm, VersionForm
from .models import Product, Version


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
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

    def get_form_class(self):
        product = self.get_object()

        if self.request.user.is_superuser:
            return OwnerProductForm  # Суперпользователь получает полную форму

        # Если текущий пользователь является владельцем продукта
        if product.owner == self.request.user:
            return OwnerProductForm  # Полная форма для владельца

        # Если текущий пользователь — модератор и имеет соответствующее разрешение
        if self.request.user.has_perm('catalog.can_change_any_product'):
            return ModeratorProductForm  # Ограниченная форма для модератора

        # Если пользователь не имеет прав для редактирования, выбросим ошибку
        raise PermissionDenied("У вас нет прав для редактирования этого продукта.")

    def get_queryset(self):
        # Модератор может редактировать все продукты, владелец только свои
        if self.request.user.has_perm('catalog.can_change_any_product'):
            return Product.objects.all()
        else:
            return Product.objects.filter(owner=self.request.user)


# class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
#     model = Product
#     fields = ('name', 'description', 'category', 'image', 'price')
#     permission_required = ('catalog.change_product',)
#     success_url = reverse_lazy('catalog:product_list')


class ProductDeLeteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()

        # Если пользователь является суперпользователем, он может удалять любой продукт
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)

        # Если текущий пользователь является владельцем продукта, ему разрешено удалять продукт
        if product.owner == request.user:
            return super().dispatch(request, *args, **kwargs)

        # Если пользователь не является владельцем и не суперпользователь, отказ в доступе
        raise PermissionDenied("У вас нет прав для удаления этого продукта.")


# class ProductDeLeteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
#     model = Product
#     permission_required = ('catalog.delete_product',)
#     success_url = reverse_lazy('catalog:product_list')


# class ProductCreateView(LoginRequiredMixin, CreateView):
#     model = Product
#     fields = ('name', 'description', 'category', 'image', 'price')
#     permission_required = ('catalog.add_product',)
#     success_url = reverse_lazy('catalog:product_list')

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
        # fields = ('name', 'description','category','image', 'price')
    success_url = reverse_lazy('catalog:product_list')


    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
