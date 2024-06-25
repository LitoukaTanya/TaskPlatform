from django.urls import path
from .views import task_create, task_detail, status_update
urlpatterns = [
    path('create/', task_create, name='task_create'),
    path('<int:pk>/', task_detail, name='task_detail'),
    path('<int:pk>/update/<str:status>/', status_update, name='status_update'),
]