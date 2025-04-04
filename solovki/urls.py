from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),
    path('news/', include('news_app2.urls')),
    path('person/', include('person.urls')),
    path('users/', include('users.urls')),
    path('map/', include('map.urls')),  # Включаем маршруты из приложения map
    path('history/', include('history.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
