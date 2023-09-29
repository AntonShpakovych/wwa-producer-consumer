from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from order_manager.models import Order
from order_manager.services.order_service import OrderService


class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    context_object_name = "order_list"
    template_name = "order/order_list.html"
    paginate_by = 10

    def get_queryset(self):
        return Order.objects.filter(employee=self.request.user)


@login_required
def delete_order(request: HttpRequest, pk: int) -> HttpResponseRedirect:
    order = get_object_or_404(Order, pk=pk)
    notification = OrderService.produce_message_notification(order=order)
    messages.info(request, notification)
    order.delete()

    return redirect("order_manager:order-list")
