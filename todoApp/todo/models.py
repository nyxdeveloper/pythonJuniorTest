from django.db import models
from django.contrib.auth.models import User
import datetime


#   модель задачи
class Todo(models.Model):
    title = models.CharField('Задача', max_length=150)
    description = models.TextField('Описание')
    deadline = models.DateField('Крайний срок выполнения', default=datetime.date.today())
    status = models.BooleanField('Статус', default=False)
    failed = models.BooleanField('Провалено', default=False)
    lastDay = models.BooleanField('Последний день', default=False)
    #   ключ привязки задачи к определенному пользователю
    todoFilter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
