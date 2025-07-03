from rest_framework import serializers
from .models import Meal , Rating

class MealSerializers(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id' , 'title' ,'description','num_of_rating' , 'avg_rating')


class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id' , 'stars' ,'user' , 'meal')
        
