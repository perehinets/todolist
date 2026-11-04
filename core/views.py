from django.shortcuts import render
from django.views import generic

from core.models import Task, Tag


class TaskList(generic.ListView):
    model = Task
    template_name = "core/index.html"


class TagList(generic.ListView):
    model = Tag
    template_name = "core/tags.html"
