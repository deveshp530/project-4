from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

    
class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workout_plan')
    what_day = models.CharField(max_length=100, default='everyday is leg day')
    workout = models.TextField()

    
