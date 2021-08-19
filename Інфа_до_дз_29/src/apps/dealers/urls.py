from django.urls import path

from src.apps.dealers.views import DealerListView, DealerDetailView, serialize_dealers

app_name = 'dealer'

urlpatterns = [
    path(
        '',
        DealerListView.as_view(),
        name='dealer_list',
    ),
    path(
        '<int:dealer_pk>/',
        DealerDetailView.as_view(),
        name='dealer_detail',
    ),
    path(
        'api/dealer/json',
        serialize_dealers,
    )
]