from rest_framework import serializers
from .models import Question, User

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = (
            'pk', 'title', 'question', 'author', 'tags', 'favorited_by', 
        )