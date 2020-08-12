from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, OrderItem, Order
from django.views.generic import ListView, DetailView, View
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


def checkout(request):
    return render(request, 'checkout.html')


class HomeView(ListView):
    model = Item
    paginate_by = 12
    template_name = 'home.html'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'product.html'


@login_required()
def add_to_cart (request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        ordered_time = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_time)
        order.items.add(order_item)
    return redirect("core:product", slug=slug)


@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("core:order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("core:product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:product", slug=slug)


class OrderSummaryView(View):
    order = OrderItem.filter(user=request.user)
    def get(self, *args, **kwargs):
        return render(self.request, 'order_summary.html')
