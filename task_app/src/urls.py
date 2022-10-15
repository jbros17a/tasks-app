from django.urls import path
from src.views import *

app_name = 'tasks'

urlpatterns = [
    path('', main, name='main')
]
