from rest_framework import serializers
from .models import Question, User, Answer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["pk", "username",]


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'pk', 'title', 'body', 'author', 'tags', 'favorited_by', 
        )

class AnswerSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    question = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        model = Answer
        fields = [
            'pk', 'question', 'answer', 'author', 'accepted'
        ]

class QuestionSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'