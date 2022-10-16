from django.urls import path
from src.views import *

app_name = 'tasks'

urlpatterns = [
    path('', TaskList.as_view(), name='main')
]
