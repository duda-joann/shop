from .views import (HomeView,
                    ItemDetailView,
                    OrderSummaryView,
                    add_to_cart,
                    remove_from_cart,
                    CheckoutView,
                    PaymentView,
                    RequestRefundView,
                    AddCouponView)
from django.urls import path


app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name = 'item-list'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('product/<slug>/', ItemDetailView.as_view(), name = 'product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-card/<slug>', remove_from_cart, name='remove-from-card'),
    path('order-summary/', OrderSummaryView.as_view(), name = 'order-summary'),
    path('payment/<payment_option>', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon')
]

