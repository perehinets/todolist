from django.shortcuts import render
from django.views import generic

from core.models import Task


class TaskList(generic.ListView):
    model = Task
    template_name = "core/index.html"


