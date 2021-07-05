from django.contrib import admin
from django.urls import path, include, re_path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks', views.tasks, name='tasks'),
    re_path(r'update_task_[0-9]*', views.update, name='update')
]

