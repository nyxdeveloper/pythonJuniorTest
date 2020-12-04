from django.urls import path

from . import views

urlpatterns = [
    path('', views.TodoList.as_view(), name='myTodos'),
    path('register/', views.RegisterFormView.as_view(), name='register'),
    path('addTodo/', views.AddTodo.as_view(), name='addTodo'),
    path('complated/', views.Complated.as_view(), name='complated'),
    path('deadline/', views.Deadline.as_view(), name='deadline'),
    path('failed/', views.Failed.as_view(), name='failed'),
    path('isTodo/', views.IsTodo.as_view(), name='isTodo'),
    path('execute/<int:el>', views.ExecuteTodo.as_view(), name='execute'),
    path('delete/<int:el>', views.DeleteTodo.as_view(), name='delete')
]