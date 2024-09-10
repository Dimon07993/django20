from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import index_list, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path('', index_list, name='product_list'),
    path('product/<int:pk>/', product_detail, name='product_detail'),


]
