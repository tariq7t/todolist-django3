from django.forms import ModelForm
from .models import Todo

# We are creating our own form for creating a todo list


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title','memo','important']