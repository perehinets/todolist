from django.urls import path

from core.views import TaskListView, TagListView, TagCreateView

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("tags/", TagListView.as_view(), name="tags"),
    path("tags/create/", TagCreateView.as_view(), name="tags-create"),
]

app_name = "core"