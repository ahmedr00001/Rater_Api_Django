from django.urls import path , include
from rest_framework import routers
from .views import RatingViewSet , MealViewSet


routers = routers.DefaultRouter()
routers.register ('meals' , MealViewSet)
routers.register ('rating' , RatingViewSet)


urlpatterns = [

    path('' , include(routers.urls))
]