from django.shortcuts import render, redirect
from django.views import View
from .forms import *
import datetime


class TodoList(View):
    def get(self, request):
        todos = Todo.objects.all()
        for i in todos:
            if datetime.date.today() > i.deadline:
                i.failed = True
            if datetime.date.today() == i.deadline:
                i.lastDay = True
        todoAddForm = TodoAddForm
        return render(request, 'todoList.html', {
            'todos': todos,
            'todoAddForm': todoAddForm,
        })


class IsTodo(View):
    def get(self, request):
        temp = Todo.objects.all()
        for i in temp:
            if datetime.date.today() > i.deadline:
                i.failed = True
            if datetime.date.today() == i.deadline:
                i.lastDay = True
        todos = []
        todoAddForm = TodoAddForm
        for i in temp:
            if not i.failed: todos.append(i)
        return render(request, 'complated.html', {
            'todos': todos,
            'todoAddForm': todoAddForm,
        })


class Complated(View):
    def get(self, request):
        temp = Todo.objects.all()
        for i in temp:
            if datetime.date.today() > i.deadline:
                i.failed = True
            if datetime.date.today() == i.deadline:
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
        temp = Todo.objects.all()
        for i in temp:
            if datetime.date.today() > i.deadline:
                i.failed = True
            if datetime.date.today() == i.deadline:
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
        temp = Todo.objects.all()
        for i in temp:
            if datetime.date.today() > i.deadline:
                i.failed = True
            if datetime.date.today() == i.deadline:
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
            boundForm.save()
            return redirect('/')
        return redirect('/')
