from django import forms

from core.models import Tag, Task


class TagCreationForm(forms.ModelForm):
    model = Tag


class TaskCreationForm(forms.ModelForm):
    model = Task
