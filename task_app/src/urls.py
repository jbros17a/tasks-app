from django.urls import path
from src.views import *

app_name = 'tasks'

urlpatterns = [
    path('', TaskList.as_view(), name='main'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('create-task/', CreateTask.as_view(), name='create'),
    path('task-edit/<int:pk>/', UpdateTask.as_view(), name='update'),
    path('task-delete/<int:pk>/', DeleteTask.as_view(), name='delete'),
]
