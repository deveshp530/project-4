from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_list, name='user_list'),
    path('workouts/<int:pk>', views.workout_list, name='workout_list'),
    path('workouts/new', views.create_workout, name='create_workout'),
    path('workouts/<int:pk>edit', views.edit_workout, name='edit_workout'),
    path('workouts/<int:pk>delete', views.delete_workout, name='delete_workout'),

]