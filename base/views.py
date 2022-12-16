from django.shortcuts import render
#returns template with query set of data
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task
from django.urls import reverse_lazy

#simple http response import
# from django.http import HttpResponse


# Create your views here.
# This is connected to urls.py and can accessed through there as well
# This looks for _list
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'

# This looks for _detail
# template name and context object name allow us to change the default naming scheme for html
# and object name
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
class DeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    