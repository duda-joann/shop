from .views import (HomeView,
                    ItemDetailView,
                    OrderSummaryView,
                    add_to_cart,
                    remove_from_cart)
from django.urls import path


app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name = 'item-list'),
    path('product/<slug>/', ItemDetailView.as_view(), name = 'product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-card/<slug>', remove_from_cart, name='remove-from-card'),
    path('order-summary/', OrderSummaryView.as_view(), name = 'order-summary'),
]

