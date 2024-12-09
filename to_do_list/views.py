# in to_do_list/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Task  # Assuming you have a Task model

def task_list(request):
    tasks = Task.objects.all()  # Fetch all tasks from the database
    return render(request, 'to_do_list/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        task_name = request.POST.get('name')
        if task_name:
            Task.objects.create(name=task_name)
            return redirect('task_list')
        # Handle task creation here (you'll likely need a form)
    
    return render(request, 'to_do_list/task_create.html')

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        # Handle task update logic here
        pass
    return render(request, 'to_do_list/task_edit.html', {'task': task})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')  # Redirect to the task list view

def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = True  # Mark the task as completed (assuming a boolean field `completed`)
    task.save()
    return redirect('task_list')  # Redirect to the task list view
