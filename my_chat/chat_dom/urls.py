from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("chat_dom/", views.chat_dom, name="chat_dom"),
]
