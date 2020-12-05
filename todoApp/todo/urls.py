from django.urls import path
from django.contrib.auth import views as authViews
from . import views

urlpatterns = [
    path('', views.TodoList.as_view(), name='myTodos'),     #   список всех задач пользователя
    path('register/', views.RegisterFormView.as_view(), name='register'),   #   форма регистрации
    path('exit/', authViews.LogoutView.as_view(next_page='/accounts/login'), name='exit'),  #   выход из аккаунта
    path('addTodo/', views.AddTodo.as_view(), name='addTodo'),  #   добавление задачи
    path('complated/', views.Complated.as_view(), name='complated'),    #   выполненные задачи пользователя
    path('deadline/', views.Deadline.as_view(), name='deadline'),   #   задачи пользователя в дедлайне
    path('failed/', views.Failed.as_view(), name='failed'),     #   проваленные задачи пользователя
    path('isTodo/', views.IsTodo.as_view(), name='isTodo'),     #   задачи пользователя с активным статусом
    path('execute/<int:el>', views.ExecuteTodo.as_view(), name='execute'),  #   подтверждение выполнения задачи
    path('delete/<int:el>', views.DeleteTodo.as_view(), name='delete')      #   удаление задачи
]