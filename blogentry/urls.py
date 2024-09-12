from django.urls import path

from  blogentry.apps import BlogentryConfig
from blogentry.views import BlogentryCreateView, BlogentryListView, BlogentryDetailView, BlogentryUpdateView, \
    BlogentryDeLeteView

app_name = BlogentryConfig.name

urlpatterns = [
    path('create/', BlogentryCreateView.as_view(), name='create'),
    path('', BlogentryListView.as_view(), name='list'),
    path('view/<int:pk>/', BlogentryDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', BlogentryUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogentryDeLeteView.as_view(), name='delete'),



]
