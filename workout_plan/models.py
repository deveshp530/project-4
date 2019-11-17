from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


# Create your models here.


    
class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workout_plan')
    what_day = models.CharField(max_length=100, default='everyday is leg day')
    workout = models.TextField()

    def __str__(self):
        return self.user

    
