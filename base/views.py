from django.shortcuts import render

#simple http response import
from django.http import HttpResponse


# Create your views here.
# This is connected to urls.py and can accessed through there as well
def taskList(request):
    return HttpResponse("To Do List")