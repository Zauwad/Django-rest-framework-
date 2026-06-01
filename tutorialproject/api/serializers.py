from rest_framework import serializers                    # Imports DRF serializers to convert model instances to/from JSON

from .models import BlogPost                    # Imports BlogPost model class from local models module


class BlogPostSerializer(serializers.ModelSerializer):                    # Serializer class mapping BlogPost model instances to JSON representation
    class Meta:                    # Inner metadata class configures serializer behavior
        model = BlogPost                    # Links this serializer to the BlogPost model class
        fields = ["id", "title", "content", "published_date"]                    # List of model attributes/fields to serialize and include in output JSON
        