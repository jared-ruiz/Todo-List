from django.urls import path
from .views import TaskList

urlpatterns = [
    # base url
    path('', TaskList.as_view(), name='tasks')
]