from django.urls import path
from src.apps.orders.views import OrderListView, DetailOrderView, serialize_orders

app_name = 'order'

urlpatterns = [
    path(
        '',
        OrderListView.as_view(),
        name='order_list',
    ),
    path(
        '<int:order_pk>/',
        DetailOrderView.as_view(),
        name='order_detail',
    ),
    path(
        'api/order/json/',
        serialize_orders,
    )
]