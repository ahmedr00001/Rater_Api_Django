from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator , MinValueValidator

class Meal(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=32)

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