from django import forms
from .models import *


class TodoAddForm(forms.Form):
    title = forms.CharField(max_length=100, label='Задача')
    deadline = forms.DateField(widget=forms.DateTimeInput)
    description = forms.CharField(max_length=2000, label='Описание', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(TodoAddForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'height': '3vh'})
        self.fields['deadline'].widget.attrs.update({'class': 'form-control', 'height': '3vh'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})

    def save(self):
        new_todo = Todo.objects.create(
            title=self.cleaned_data['title'],
            deadline=self.cleaned_data['deadline'],
            description=self.cleaned_data['description'],
            status = Status(title='is todo', styleKey='primary')
        )
        return new_todo