from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import WorkoutPlan,User
from .forms import WorkoutForm

# Create your views here.
def user_list(request):
    user = User.objects.all()
    return render(request, 'workout/user_list.html', {'user' : user})

def workout_list(request, pk):
    workout = WorkoutPlan.objects.get(id=pk)
    return render(request, 'workout/workout_list.html', {'workout' : workout})

@login_required
def create_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save()
            return redirect('workout_list', pk=workout.pk)
    else:
        # initial ={'user': request.user.username}
        form = WorkoutForm(initial ={'user': request.user.username})
    return render(request, 'workout/workout_form.html', {'form': form})
    
def edit_workout(request,pk):
    workout = WorkoutPlan.objects.get(id=pk)
    if request.method == 'POST':
        form = WorkoutForm(request.POST, instance=workout)
        if form.is_valid():
            workout = form.save()
            return redirect('workout_list', pk=workout.pk)
    else:
        # initial = {'user': request.user.username}        
        form = WorkoutForm(initial ={'user': request.user.username}, instance=workout)
    return render(request, 'workout/workout_form.html', {'form': form})

@login_required
def delete_workout(request,pk):
    WorkoutPlan.objects.get(id=pk).delete()
    User.objects.get(id=pk).delete()
    return redirect('user_list')



 