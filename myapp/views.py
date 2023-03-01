from turtle import title
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, JsonResponse

from myapp.forms import CreateNewTask
from .models import Project,Task
# Create your views here.
def index(request):
    title = 'Django Course'
    return render(request,"index.html",{
        'title':title
    })
    
def about(request):
    username= "hola"
    return render(request,"about.html",{
        'username':username
    })

def hello(request,username):
    return HttpResponse("<h1>hello %s</h1>" %username)


def projects(request):
    projects = Project.objects.all()
    return render(request,"projects.html",{
        'projects':projects
    })

    # projects = list(Project.objects.values())
    #return JsonResponse(projects,safe=False)
    # return HttpResponse("projects")

def tasks(request,id=0):
    #task = Task.objects.get(id=id)
    # task = get_object_or_404(Task,id=id) // para retornar 404 si salta un error
    # return HttpResponse("tasks %s" %task.title).

       # projects = list(Project.objects.values())
    tasks = Task.objects.all()
    return render(request,"tasks.html",{
        'tasks':tasks
    })

def create_task(request) :

    if request.method == 'GET':
        return render(request,'create_task.html', {'form':CreateNewTask()})
    else:
        Task.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            project_id=1
        )
        return redirect('/tasks')
    
def demo(request):
    username = "Jose"
    return HttpResponse("<h1>hello %s</h1>" %username)
