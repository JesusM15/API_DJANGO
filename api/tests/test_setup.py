from rest_framework.test import APITestCase #clase para realizar pruebas unitarias en djangorestframework
from rest_framework import status

class TestSetUp(APITestCase):
    
    #metodo que inicializa la clase
    def setUp(self):
        from users.models import User
        
        #url para que se loguee y obtenga el token
        self.login_url = '/api/token/'
        #crear un usuario para realizar las pruebas
        self.user = User.objects.create_superuser(name='usuario', last_name='de prueba', username='Usuario', password='Usuario123', email='pruebas@gmail.com')
        
        # self.client instancia de la clase client
        #metodo post para realizar un post a una ruta
        response = self.client.post(
                self.login_url,
                {
                    'username': self.user.username,
                    'password': 'Usuario123'
                },
                format='json'
            ) 
        
        #evaluar si la de la peticion de token fue exitosa
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        #print(response.data['access'])
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        
        return super().setUp()