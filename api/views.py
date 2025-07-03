from rest_framework import viewsets , status
from .models import Meal , Rating
from .serializers import MealSerializers , RatingSerializers , UserSerializers

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import request
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny ,IsAuthenticated ,IsAdminUser ,IsAuthenticatedOrReadOnly
 
from django.contrib.auth.models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated ]

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializers

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated ]


    @action(methods=['post'] , detail=True)
    def rate_meal(self , request , pk=None):
        if 'stars' in request.data:
            '''
            create or update
            always when you find or use try
            '''
            meal = Meal.objects.get(id=pk)
            user = request.user
            print(user)
            # username = request.data['username']
            # user = User.objects.get(username=username)
            stars = request.data['stars']
            try:
                 #update
                rating = Rating.objects.get(user=user, meal=meal) 
                rating.stars =stars
                rating.save()
                serializer = RatingSerializers(rating , many= False)
                json = {
                     'message': 'Meal Rate updated',
                     'result': serializer.data     
                }
                return Response(json , status=status.HTTP_200_OK)
               
            except:
                 #create if rate not exist
                 rating = Rating.objects.create(user = user , meal= meal, stars=stars)
                 serializer = RatingSerializers(rating , many= False)
                 json = {
                     'message': 'Meal Rate Created',
                     'result': serializer.data     
                 }
                 return Response(json , status=status.HTTP_200_OK) 

        else:
                json ={
                     'message' :'starts not provided'
                }
                return Response(json , status=status.HTTP_400_BAD_REQUEST)
    

class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    #just for override defult update to not use
    def update(self, request, *args, **kwargs):
         response = {
              'message' : 'this in not how you create/update rating'
         }
         return Response (response , status=status.HTTP_400_BAD_REQUEST)
   
   
    #just for override defult update to not use
    def create(self, request, *args, **kwargs):
         response = {
              'message' : 'this in not how you create/update rating'
         }
         return Response (response , status=status.HTTP_400_BAD_REQUEST)
