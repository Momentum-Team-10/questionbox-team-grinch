from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

class User(AbstractUser):
    def __repr__ (self):
        return f"<User username={self.username} pk={self.pk}>"

    def __str__(self):
        return self.username

class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.tag


class Question(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questions")
    # list of strings
    favorited_by = models.ManyToManyField(
        User, related_name="favorite_questions", blank=True
    )
    # list of strings
    tags = models.ManyToManyField(
        to=Tag, related_name="questions", blank=True
    )


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    answer = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="answers")
    accepted = models.BooleanField(default=False)
    favorited_by = models.ManyToManyField(
        User, related_name="favorite_answers", blank=True
    )