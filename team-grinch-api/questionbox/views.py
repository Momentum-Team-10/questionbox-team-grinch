from django.db.models import query
from django.shortcuts import render
from rest_framework.decorators import permission_classes
from .serializers import QuestionSerializer, AnswerSerializer
from .models import Question, User, Answer
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView, CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView  
from rest_framework.viewsets import ModelViewSet

from questionbox import permissions, serializers


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
    #queryset = Answer.objects.all().order_by("accepted").reverse()
    serializer_class = AnswerSerializer
    permission_classes = []

    def perform_create(self, serializer):
        question = Question.objects.get(pk=self.kwargs['questions_pk'])
        serializer.save(author=self.request.user, question=question)

    def get_queryset(self):
        question = Question.objects.get(
            pk=self.kwargs['questions_pk']
        )
        queryset = question.answers.all()
        return queryset


