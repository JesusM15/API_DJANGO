
from api.models import Task

class TasksFactory:
    
    #crear el JSON para la tarea falsa a crear
    def build_tasks_JSON(self):
        return {
            'title': 'Hacer compras',
            'description': 'Ir a hacer compras el jueves',
            'done': False, 
        }
    
    def create_tasks(self):
        return Task.objects.create(**self.build_tasks_JSON())
