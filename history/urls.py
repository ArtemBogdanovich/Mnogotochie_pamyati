from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.history_list, name='history_list'),
    path('<int:pk>', views.DetailHistory.as_view(), name='history')
]