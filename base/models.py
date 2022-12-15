from django.db import models

#built in django models
from django.contrib.auth.models import User
# Create your models here.

# models
class Task(models.Model):
    # if user is deleted, items associated will be deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    #string representation of model
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']