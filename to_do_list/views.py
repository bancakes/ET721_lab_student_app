# in to_do_list/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Task  # Assuming you have a Task model

def task_list(request):
    tasks = Task.objects.all()  # Fetch all tasks from the database
    return render(request, 'to_do_list/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        task_title = request.POST.get('title')
        if task_title:
            Task.objects.create(title=task_title)
            return redirect('task_list')
        # Handle task creation here (you'll likely need a form)
    
    return render(request, 'to_do_list/task_create.html')

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        # Handle task update logic here
        pass
    return render(request, 'to_do_list/task_edit.html', {'task': task})

def task_confirm_delete(request, item_id):
    task = get_object_or_404(Task, pk=item_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')  # Redirect to the task list after deletion
    return render(request, 'to_do_list/task_confirm_delete.html', {'task': task})

def task_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.completed = True  # Mark the task as completed (assuming a boolean field `completed`)
    task.save()
    return redirect('task_list')  # Redirect to the task list view

def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task_title = request.POST.get('title')
        task_description = request.POST.get('description')
        task_completed = request.POST.get('completed') == 'on'  # Check if checkbox is checked

        if task_title:  # Ensure the title is provided
            task.title = task_title
            task.description = task_description
            task.completed = task_completed
            task.save()  # Save the changes to the task
            return redirect('task_list')  # Redirect to the task list after saving changes
    
    return render(request, 'to_do_list/task_edit.html', {'task': task})
