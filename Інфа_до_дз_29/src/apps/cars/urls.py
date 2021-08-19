from django.urls import path

from src.apps.cars.views import CarListView, CarsDetailBoardView, serialize_car

app_name = 'cars'

urlpatterns = [
    path(
        '',
        CarListView.as_view(),
        name='car_list',
    ),
    path(
        '<slug:car_slug>/',
        CarsDetailBoardView.as_view(),
        name='car_detail',
    ),
    path(
        'api/car/json/',
        serialize_car,
    )
]