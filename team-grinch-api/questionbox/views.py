from django.shortcuts import render
from rest_framework.decorators import permission_classes
from .serializers import QuestionSerializer, AnswerSerializer
from .models import Question, User, Answer
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView  
from rest_framework.viewsets import ModelViewSet


class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all().order_by("title")
    serializer_class = QuestionSerializer
    permission_classes = []

    def get_serializer_class(self):
        if self.action in ["list"]:
            return QuestionSerializer
        return super().get_serializer_class()
    
    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user.pk)

class AnswerViewSet(ModelViewSet):
    queryset = Answer.objects.all().order_by("accepted")
    serializer_class = AnswerSerializer
    permission_classes = []

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)