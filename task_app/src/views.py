from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from .models import Task

class TaskList(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'