from django.urls import path, re_path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("add", views.add, name="add"),
    path("view", views.view, name="view"),
    path("git", views.gitcontrol, name="gitcont"),
    path("delete", views.deleteid, name="deleteid")
]
