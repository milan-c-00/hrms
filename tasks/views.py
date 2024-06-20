from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import Task
from .forms import TaskForm
from .models import Employee
from django.db.models import Q
from django.db.models import Case, When, Value, CharField




def alltasks(request):
    query = request.GET.get('q')
    
    # Fetch all tasks or filter by search query
    if query:
        tasks = Task.objects.filter(
            Q(title__icontains=query) |
            Q(status__icontains=query) |
            Q(start__icontains=query) |
            Q(end__icontains=query) |
            Q(employee__first_name__icontains=query) |
            Q(employee__last_name__icontains=query) |
            Q(importance__icontains=query)
        )
    else:
        tasks = Task.objects.all()
    
    # Define custom ordering by importance
    custom_ordering = Case(
        When(importance='High', then=Value(1)),
        When(importance='Medium', then=Value(2)),
        When(importance='Low', then=Value(3)),
        default=Value(4),
        output_field=CharField(),
    )
    
    # Categorize and sort tasks by status and importance
    to_do_tasks = tasks.filter(status='To Do').order_by(custom_ordering)
    in_progress_tasks = tasks.filter(status='In Progress').order_by(custom_ordering)
    completed_tasks = tasks.filter(status='Completed').order_by(custom_ordering)
    
    return render(request, 'tasks/alltasks.html', {
        'to_do_tasks': to_do_tasks,
        'in_progress_tasks': in_progress_tasks,
        'completed_tasks': completed_tasks,
    })


def add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tasks/') 
        else:
            print(form.errors)
         
    else:
        form = TaskForm()
    return render(request, 'tasks/add.html', {'form': form})

def taskdetail(request, task_id):
    task_instance = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task_instance)
        if form.is_valid():
            form.save()
            return redirect('/tasks/')
    else:
        form = TaskForm(instance=task_instance)

    return render(request, 'tasks/taskdetail.html', {'task': task_instance, 'form': form})





    