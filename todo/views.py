from django.shortcuts import render, get_object_or_404, redirect
from .models import TodoItem
from .forms import TodoItemForm

def todo_list(request):
    tasks = TodoItem.objects.all()
    return render(request, 'todo/todo_list.html', {'tasks': tasks})

def todo_detail(request, id):
    task = get_object_or_404(TodoItem, id=id)
    return render(request, 'todo/todo_detail.html', {'task': task})

def todo_create(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoItemForm()
    return render(request, 'todo/todo_form.html', {'form': form})

def todo_edit(request, id):
    task = get_object_or_404(TodoItem, id=id)
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoItemForm(instance=task)
    return render(request, 'todo/todo_form.html', {'form': form})

def todo_delete(request, id):
    task = get_object_or_404(TodoItem, id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('todo_list')
    return render(request, 'todo/todo_confirm_delete.html', {'task': task})
