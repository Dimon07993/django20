from django.conf import settings
from django.templatetags.static import static
from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductCreateView, ProductListView, ProductDetailView, ProductUpdateView, ProductDeLeteView

app_name = CatalogConfig.name

urlpatterns = [

path('', ProductListView.as_view(), name='product_list'),
path('create/', ProductCreateView.as_view(), name='create'),
path('view/<int:pk>/', ProductDetailView.as_view(), name='view'),
path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit'),
path('delete/<int:pk>/', ProductDeLeteView.as_view(), name='delete'),
]





#urlpatterns = [
#    path('', ProductListView.as_view(), name='product_list'),
#    path('view/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
#    path('create/', ProductCreateView.as_view(), name='create_product'),
#    path('edit/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
#]
#urlpatterns = [
#    path('', index_list, name='product_list'),
#    path('product/<int:pk>/', product_detail, name='product_detail'),
#    path('create/', ProductCreateView.as_view(), name='create_product'),
#
#
#]
