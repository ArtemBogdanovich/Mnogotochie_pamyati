from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.person_list, name = 'person_list'),
    path('create_person', views.create_person, name='person_create'),
    path('<int:pk>/', views.PersonDetail.as_view(), name = 'person-page' ),
    path('<int:pk>/delete', views.PersonDelete.as_view(), name = 'person-delete' ),
    path('<int:pk>/update', views.PersonUpdate.as_view(), name = 'person-update' )

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
