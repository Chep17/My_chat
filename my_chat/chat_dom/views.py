from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from . import models


def index(request):
    return HttpResponse("Hello, world.")


def chat_dom(request):
    chat_dom = models.Chat.objects.all()
    context = {
        "chat_dom": chat_dom,
    }
    return render(request, "chat_dom.html", {"context": context})
