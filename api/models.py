from django.db import models
from users.models import User

#modelo para las tareas
class Task(models.Model):
    #atributos de las tareas
    title = models.CharField(max_length=255) 
    description = models.TextField(blank=True)
    done = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):return f'{self.title}'
    
    class Meta:
        ordering = ['-created']
    