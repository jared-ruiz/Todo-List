from django.urls import path
from . import views

urlpatterns = [
    # base url
    path('', views.taskList, name='tasks')
]