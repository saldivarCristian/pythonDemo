from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('hello/<str:username>', views.hello),
    # path('hello/<int:id>', views.hello),
    path('about', views.about, name="about"),
    path('projects', views.projects, name="projects"),
    path('projects/<int:id>', views.projects_detail, name="projects_detail"),
    path('tasks', views.tasks, name="tasks"),
    path('create_task', views.create_task),
    path('create_projects', views.create_projects, name="create_projects"),
    path('demo', views.demo),
    path('contacto', views.contact),
]
