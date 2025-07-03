from django.urls import path , include
from rest_framework import routers
from .views import RatingViewSet , MealViewSet , UserViewSet




router = routers.DefaultRouter()
router.register ('meals' , MealViewSet)
router.register ('rating' , RatingViewSet)
router.register ('users' , UserViewSet)



urlpatterns = [

    path('' , include(router.urls))
]