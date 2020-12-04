from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.views import View
from .forms import *
import datetime


class RegisterFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "account/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "register.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


class TodoList(View):
    def get(self, request):
        todos = Todo.objects.filter(todoFilter=self.request.user)
        for i in todos:
            if datetime.date.today() > i.deadline:
                if not i.status:
                    i.failed = True
            if datetime.date.today() == i.deadline:
                if not i.status:
                    i.lastDay = True
        todoAddForm = TodoAddForm
        return render(request, 'todoList.html', {
            'todos': todos,
            'todoAddForm': todoAddForm,
        })


class IsTodo(View):
    def get(self, request):
        temp = Todo.objects.filter(todoFilter = self.request.user)
        for i in temp:
            if datetime.date.today() > i.deadline:
                if not i.status:
                    i.failed = True
            if datetime.date.today() == i.deadline:
                if not i.status:
                    i.lastDay = True
        todos = []
        todoAddForm = TodoAddForm
        for i in temp:
            if not i.failed and not i.status: todos.append(i)
        return render(request, 'complated.html', {
            'todos': todos,
            'todoAddForm': todoAddForm,
        })


class Complated(View):
    def get(self, request):
        temp = Todo.objects.filter(todoFilter = self.request.user)
        for i in temp:
            if datetime.date.today() > i.deadline:
                if not i.status:
                    i.failed = True
            if datetime.date.today() == i.deadline:
                if not i.status:
                    i.lastDay = True
        todos = []
        todoAddForm = TodoAddForm
        for i in temp:
            if i.status: todos.append(i)
        return render(request, 'complated.html', {
            'todos': todos,
            'todoAddForm': todoAddForm,
        })


class Deadline(View):
    def get(self, request):
        temp = Todo.objects.filter(todoFilter = self.request.user)
        for i in temp:
            if datetime.date.today() > i.deadline:
                if not i.status:
                    i.failed = True
            if datetime.date.today() == i.deadline:
                if not i.status:
                    i.lastDay = True
        todos = []
        todoAddForm = TodoAddForm
        for i in temp:
            if i.lastDay: todos.append(i)
        return render(request, 'deadline.html', {
            'todos': todos,
            'todoAddForm': todoAddForm,
        })


class Failed(View):
    def get(self, request):
        temp = Todo.objects.filter(todoFilter = self.request.user)
        for i in temp:
            if datetime.date.today() > i.deadline:
                if not i.status:
                    i.failed = True
            if datetime.date.today() == i.deadline:
                if not i.status:
                    i.lastDay = True
        todos = []
        todoAddForm = TodoAddForm
        for i in temp:
            if i.failed: todos.append(i)
        return render(request, 'complated.html', {
            'todos': todos,
            'todoAddForm': todoAddForm,
        })


class AddTodo(View):
    def post(self, request):
        boundForm = TodoAddForm(request.POST)
        if boundForm.is_valid():
            boundForm.save(request)
            return redirect('/')
        return redirect('/')


class DeleteTodo(View):
    def get(self, request, el):
        Todo.objects.get(id=el).delete()
        return redirect('/')


class ExecuteTodo(View):
    def get(self, request, el):
        todo = Todo.objects.get(id=el)
        todo.status = True
        Todo.objects.get(id=el).delete()
        todo.save()
        return redirect('/')
