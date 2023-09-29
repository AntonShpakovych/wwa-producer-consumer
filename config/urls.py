from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", RedirectView.as_view(url="orders/", permanent=True)),
    path("orders/", include("order_manager.urls", namespace="order_manager")),
]


handler404 = "config.views.handler_404"
