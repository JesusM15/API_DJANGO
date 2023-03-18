from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework import routers
#nos permite definir de manera rapida un enrutador para nuestros viewsets
from rest_framework_extensions.routers import ExtendedSimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import TaskViewSet, UserViewSet

router: ExtendedSimpleRouter = ExtendedSimpleRouter()

router = routers.DefaultRouter()
#para generar los urls teniendo en cuenta el tipo de peticion HTTP a realizar
router.register(r'tasks', TaskViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger/', SpectacularSwaggerView.as_view(url_name="api:schema"), name='swagger'),
    #manejar el token con las vistas de JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    #Incluye las vistas de 
    path('', include(router.urls)),
    
]