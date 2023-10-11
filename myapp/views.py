from django.shortcuts import render, redirect
from .models import Task

# Create your views here.
def tasks(request):
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {'tasks':tasks})


def add_tasks(request):
    if request.method == 'POST':
        task = request.POST
        add = Task.objects.create(body=task['body'], description=task['description'])
        add.save()
        return redirect('tasks')
    else:
        return render(request, 'add_task.html')