from django.urls import path

from order_manager.views import OrderListView, delete_order


urlpatterns = [
    path("", OrderListView.as_view(), name="order-list"),
    path("<int:pk>/", delete_order, name="order-delete")
]

app_name = "order_manager"
