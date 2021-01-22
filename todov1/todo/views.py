from django.shortcuts import render, redirect

from . import models

# Create your views here.
def todo_list(request):
    tasks = models.Todo.objects.all()
    template_data = {
        'task_list':tasks
    }
    return render(request,'todo_list.html',template_data)

def todo_add(request):
    task_name = request.POST.get('task_name')
    new_task = models.Todo.objects.create(task = task_name)
    new_task.save()
    return redirect('todo-list')

def remove_todo(request, task_id):
    task_to_deleted = models.Todo.objects.get(id=task_id)
    task_to_deleted.delete()
    return redirect('todo-list')