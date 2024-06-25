from django import forms
from .models import Task, User, Comment
from django.contrib.auth.forms import UserCreationForm


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['name', 'description', 'assignee', 'end_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['assignee'].queryset = User.objects.all()


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']
