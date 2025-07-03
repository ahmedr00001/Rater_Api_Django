from rest_framework import serializers
from .models import Meal , Rating
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class MealSerializers(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id' , 'title' ,'description','num_of_rating' , 'avg_rating')
        


class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id' , 'stars' ,'user' , 'meal')



class UserSerializers(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'token', 'password']
        extra_kwargs = {
            'password': {'write_only': True, 'required': True}
        }

    def get_token(self, user):
        token, _ = Token.objects.get_or_create(user=user)
        return token.key

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

            
