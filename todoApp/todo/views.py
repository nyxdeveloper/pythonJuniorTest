from django.shortcuts import render, redirect
from django.views import View
from .models import *
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


class AddTodo(View):
    def post(self, request):
        boundForm = TodoAddForm(request.POST)
        if boundForm.is_valid():
            boundForm.save()
            return redirect('/')
        return redirect('/')