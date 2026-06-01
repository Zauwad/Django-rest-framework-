from rest_framework import serializers                    # Imports DRF serializers to convert model instances to/from JSON
from tutorialproject.todos.models import BlogPost                    # Imports BlogPost model class (Note: currently empty/not defined in todos.models)


class BlogPostSerializer(serializers.ModelSerializer):                    # Serializer class mapping BlogPost model instances to JSON representation
    class Meta:                    # Inner metadata class configures serializer behavior
        model = BlogPost                    # Links this serializer to the BlogPost model class
        field = ["id", "title","content","published_data"]                    # Declares serializer fields (Note: field is a typo for fields, and published_data for published_date)
        