from django import forms

from core.models import Tag


class TagCreationForm(forms.ModelForm):
    model = Tag
