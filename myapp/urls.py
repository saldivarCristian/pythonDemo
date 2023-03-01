from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('hello/<str:username>', views.hello),
    # path('hello/<int:id>', views.hello),
    path('about', views.about),
    path('projects', views.projects),
    path('tasks', views.tasks),
    path('create_task', views.create_task),
    path('demo', views.demo),
]
