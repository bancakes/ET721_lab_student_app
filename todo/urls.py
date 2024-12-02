from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('todo/<int:id>/', views.todo_detail, name='todo_detail'),
    path('todo/new/', views.todo_create, name='todo_create'),
    path('todo/<int:id>/edit/', views.todo_edit, name='todo_edit'),
    path('todo/<int:id>/delete/', views.todo_delete, name='todo_delete'),
]
