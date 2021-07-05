from django.http.response import HttpResponse
from django.shortcuts import render
from home.models import Tasks
import re

# Create your views here.
def home(request):
    context = {'success': False}
    if request.method == 'POST':
        title = request.POST['task_title']
        desc = request.POST['task_desc']
        task = Tasks(task_title=title, task_desc=desc)
        task.save()
        context = {'success': True}
    # return HttpResponse("This is my contacts page (/contacts)")  
    return render(request, 'index.html', context)


def tasks(request):
    all_tasks = Tasks.objects.all()
    context = {'tasks': all_tasks}
    return render(request, 'tasks.html', context)


def update(request):
    full_path = re.search(r"update_task_([0-9]*)", request.get_full_path())
    id = full_path.group(1)
    context = {'success': False, 'id': id}
    if request.method == 'POST':
        # t = Tasks.objects.get(id=id)
        # t.task_title = request.POST['task_title']
        # t.task_desc = request.POST['task_desc']
        # t.save()
        # context = {'success': True}
        task_title = request.POST['task_title']
        task_desc = request.POST['task_desc']
        print(task_title, task_desc)
    else:
        print('NO more')
    # return HttpResponse("This is my contacts page (/contacts)")  
    return render(request, 'update.html', context)