from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path("", include("catalog.urls", namespace="catalog")),
    path("blogentry/", include("blogentry.urls", namespace="blogentry")),
    path("users/", include("users.urls", namespace="users")),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


