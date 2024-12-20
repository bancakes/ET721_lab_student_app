
from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # Now the task list will be at '/tasks/'
    path('create/', views.task_create, name='task_create'),
    path('edit/<int:pk>/', views.task_update, name='task_update'),
    path('delete/<int:item_id>/', views.task_confirm_delete, name='task_confirm_delete'),
    path('complete/<int:pk>/', views.task_complete, name='task_complete'),
    path('edit/<int:task_id>/', views.task_edit, name='task_edit'),
]
