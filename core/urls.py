from django.urls import path

from core.views import TaskList

urlpatterns = [
    path("", TaskList.as_view(), name="home"),
]