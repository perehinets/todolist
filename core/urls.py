from django.urls import path

from core.views import TaskList, TagList

urlpatterns = [
    path("", TaskList.as_view(), name="home"),
    path("tags/", TagList.as_view(), name="tags"),
]