from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoList.as_view(), name='myTodos'),
    path('addTodo/', views.AddTodo.as_view(), name='addTodo')
]