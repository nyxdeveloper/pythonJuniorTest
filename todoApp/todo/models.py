from django.db import models
import datetime


class Status(models.Model):
    title = models.CharField(max_length=50)
    styleKey = models.CharField(max_length=50)

    def __init__(self, title, styleKey, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = title
        self.styleKey = styleKey

    def __str__(self):
        return self.title


class Todo(models.Model):
    title = models.CharField('Задача', max_length=150)
    description = models.TextField('Описание')
    deadline = models.DateField('Крайний срок выполнения', default=datetime.date.today())
    status = models.ManyToManyField(Status, 'Статус')

    def __str__(self):
        return self.title



