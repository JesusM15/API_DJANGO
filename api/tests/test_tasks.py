from .test_setup import TestSetUp
from api.models import Task
from rest_framework import status
from .tasks_for_tests.tasks import TasksFactory

class TaskTestCase(TestSetUp):
    
    url = '/api/'
    
    #prueba para ver si se puede obtener una tarea por su ID correctamente
    def test_get_task(self):
        task = TasksFactory().create_tasks()
        
        response = self.client.get(
            self.url + 'tasks/',
            {'id': task.id,},
            format='json'            
        )         
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['id'], task.id)
        
    #crear tareas
    def test_new_task(self):
        task = TasksFactory().build_tasks_JSON()
        response = self.client.post(
            self.url + 'tasks/',
            task,
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.all().count(), 1)        
        
    #eliminar tareas
    def test_delete_task(self):
        task = TasksFactory().create_tasks()
        dict = Task.objects.all()
        response = self.client.delete(
            f'{self.url}tasks/{task.id}/',
        )
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(dict.count(), 0)
        
    #actualizar tarea
    def test_update_task(self):
        task = TasksFactory().create_tasks()
        response = self.client.put(
            f'{self.url}tasks/{task.id}/',
            data={'title': 'Titulo actualizado',},
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Titulo actualizado')
        
        
