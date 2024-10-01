from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductCreateView, ProductListView, ProductDetailView, ProductUpdateView, ProductDeLeteView

app_name = CatalogConfig.name

urlpatterns = [

    path('', cache_page(60 * 15)(ProductListView.as_view()), name='product_list'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('view/<int:pk>/', cache_page(60 * 15)(ProductDetailView.as_view()), name='view'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', ProductDeLeteView.as_view(), name='delete'),
]
