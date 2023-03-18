from django.shortcuts import render
from users.models import User
#para utilizar el Swagger
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

#serializers y modelos
from .serializers import TaskSerializer, UserSerializer
from .models import Task

#permite manipular los titulos, descripciones, tipos de datos
#seran lo que permitira el CRUD y la descripcion que aparecera graficamente sobre la accion.
@extend_schema_view(
    #get
    list=extend_schema(description="Esta URL permite obtener una lista de tareas"),
    retrieve=extend_schema(description="Esta URL permite obtener una tarea por medio de su ID."),
    #post
    create=extend_schema(description="Esta URL permite crear una tarea."),
    #put
    update=extend_schema(description="Esta URL permite actualizar una tarea."),
    #delete
    destroy=extend_schema(description="Esta URL permite eliminar una tarea."),
)

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    

