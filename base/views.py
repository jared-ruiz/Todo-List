from django.shortcuts import render
#returns template with query set of data
from django.views.generic.list import ListView
from .models import Task

#simple http response import
# from django.http import HttpResponse


# Create your views here.
# This is connected to urls.py and can accessed through there as well
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    