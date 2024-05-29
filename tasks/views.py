from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import Task
from .forms import TaskForm
from .models import Employee

def alltasks(request):
    to_do_tasks = Task.objects.filter(status='To Do')
    in_progress_tasks = Task.objects.filter(status='In Progress')
    completed_tasks = Task.objects.filter(status='Completed')
    
    context = {
        'to_do_tasks': to_do_tasks,
        'in_progress_tasks': in_progress_tasks,
        'completed_tasks': completed_tasks,
    }
    return render(request, 'tasks/alltasks.html', context)

def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.employee_id = form.cleaned_data['employee'].id
            task.save()
            return redirect('/tasks/')
    else:
        form = TaskForm()
    return render(request, 'tasks/create.html', {'form': form})




    