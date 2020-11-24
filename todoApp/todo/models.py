from django.db import models
import datetime


class Todo(models.Model):
    title = models.CharField('Задача', max_length=150)
    description = models.TextField('Описание')
    deadline = models.DateField('Крайний срок выполнения', default=datetime.date.today())
    status = models.BooleanField('Статус', default=False)
    failed = models.BooleanField('Провалено', default=False)
    lastDay = models.BooleanField('Последний день', default=False)

    def __str__(self):
        return self.title



