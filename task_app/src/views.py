from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Task

class TaskList(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'


class CreateTask(CreateView):
    model = Task
    template_name = 'task_form.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks:main')


class UpdateTask(UpdateView):
    model = Task
    template_name = 'task_form.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks:main')


class DeleteTask(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks:main')
    template_name = 'task_delete_confirm.html'