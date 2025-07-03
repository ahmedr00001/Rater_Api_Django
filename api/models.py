from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator , MinValueValidator

class Meal(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=32)
    def num_of_rating(self):
         rating = Rating.objects.filter(meal =self)

         return len(rating)
    
    def avg_rating(self):
         #sum/lengh
         sum =0 #initial by zero
         rating = Rating.objects.filter(meal =self) #num of rating to meal
         for rate in rating:
              sum += rate.stars
              if len(rating) >0:
                return float(sum/len(rating))
              else:
                   return 0
         


    def __str__(self):
        return self.title
    

class Rating(models.Model):
    meal = models.ForeignKey(Meal , on_delete=models.CASCADE)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[
         MinValueValidator(1),
         MaxValueValidator(5),
        ])

    # def __str__(self):
    #     return self.meal
    

    #user can only make one rate to each meal 
    class Meta:
            constraints = [
                models.UniqueConstraint(fields=['user', 'meal'], name='unique_user_meal_combination')
            ]
            indexes = [
                models.Index(fields=['user', 'meal'], name='user_meal_index')
            ]