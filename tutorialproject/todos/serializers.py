from rest_framework import serializers
from tutorialproject.todos.models import BlogPost


class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        field = ["id", "title","content","published_data"]
        