from django import forms
from .models import *


class TodoAddForm(forms.Form):
    title = forms.CharField(max_length=100)
    deadline = forms.DateField(widget=forms.SelectDateWidget)
    description = forms.CharField(max_length=2000, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(TodoAddForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control m-2', 'height': '3vh', 'placeholder': 'Задача'})
        self.fields['deadline'].widget.attrs.update(
            {'class': 'form-control w-25 m-2', 'style': 'width: 33%; display: inline-block;', 'height': '3vh'})
        self.fields['description'].widget.attrs.update({'class': 'form-control m-2', 'placeholder': 'Описание'})

    def save(self):
        new_todo = Todo.objects.create(
            title=self.cleaned_data['title'],
            deadline=self.cleaned_data['deadline'],
            description=self.cleaned_data['description']
        )
        return new_todo
