from django import forms
from .models import WorkoutPlan, User
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = WorkoutPlan
        fields = ('user', 'what_day','workout')

# class CustomUserCreationForm(UserCreationForm):

#     class Meta:
#         model = User
#         fields = ('username', 'email')

# class CustomUserChangeForm(UserChangeForm):

#     class Meta:
#         model = User
#         fields = ('username', 'email')

