from django import forms
from .models import WorkoutPlan

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = WorkoutPlan
        fields = ('user', 'what_day','workout')

