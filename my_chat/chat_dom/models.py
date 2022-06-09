from django.contrib.auth.models import User
from django.db import models


class Chat(models.Model):
    name_chat = models.CharField(max_length=255)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name_chat


class Mesages(models.Model):
    id_chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    id_users = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text
