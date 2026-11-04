from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from core.forms import TagCreationForm
from core.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    template_name = "core/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('core:home')


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('core:home')

class TagListView(generic.ListView):
    model = Tag
    template_name = "core/tags.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy('core:tags')


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy('core:tags')


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy('core:tags')
