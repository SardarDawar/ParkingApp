from django.urls import path
from .views import update_cars,car_charge,car_left,park_hist,car_remove,Car_type


urlpatterns = [
    path("",update_cars),
    path("<str:id>/delete/",car_left),
    path("<str:id>/charge/",car_charge),
    path("history/",park_hist),
    path("remove/",car_remove),    
    path("type/<str:let>/",Car_type)
]