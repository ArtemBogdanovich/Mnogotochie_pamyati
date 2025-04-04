from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MapInfoViewSet, mapq, create_point

router = DefaultRouter()
router.register(r'map', MapInfoViewSet, basename='mapinfo')

urlpatterns = [
    path('api/', include(router.urls)),  # Включаем маршруты, сгенерированные router
    path('', mapq, name='map'),  # Маршрут для вашего HTML шаблона по умолчанию
    path('update/', create_point, name='create_point')  # Маршрут для создания точки
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
