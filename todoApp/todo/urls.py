from django.urls import path

from . import views

urlpatterns = [
    path('', views.TodoList.as_view(), name='myTodos'),
    path('addTodo/', views.AddTodo.as_view(), name='addTodo'),
    path('complated/', views.Complated.as_view(), name='complated'),
    path('deadline/', views.Deadline.as_view(), name='deadline'),
    path('failed/', views.Failed.as_view(), name='failed'),
    path('isTodo/', views.IsTodo.as_view(), name='isTodo')
]