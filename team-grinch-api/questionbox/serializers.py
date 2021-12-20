from rest_framework import serializers
from .models import Question, User, Answer

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = (
            'pk', 'title', 'body', 'author', 'tags', 'favorited_by', 
        )

class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field="username")
    
    class Meta:
        model = Answer
        fields = [
            'pk', 'answer', 'author', 'accepted'
        ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["pk", "username"]

