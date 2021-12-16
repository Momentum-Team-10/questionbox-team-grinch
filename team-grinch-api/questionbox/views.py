from django.db.models.query import QuerySet
from django.shortcuts import render
from rest_framework.decorators import permission_classes
from .serializers import QuestionSerializer
from .models import Question, User
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView  
from rest_framework.viewsets import ModelViewSet


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all().order_by("title")
    serializer_class = QuestionSerializer
    permission_classes = []

    def get_serializer_class(self):
        if self.action in ["list"]:
            return QuestionSerializer
        return super().get_serializer_class()


