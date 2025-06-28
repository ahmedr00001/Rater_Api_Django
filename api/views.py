from rest_framework import viewsets
from .models import Meal , Rating
from .serializers import MealSerializers , RatingSerializers

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializers


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers
