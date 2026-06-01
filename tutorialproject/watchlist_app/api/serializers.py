from rest_framework import serializers                    # Imports DRF serializers to convert model instances to/from JSON
from watchlist_app.models import Movie                    # Imports Movie model class from local watchlist_app models


class MovieSerializer(serializers.Serializer):                    # Serializer class defining fields and validation logic for Movie instances
    id = serializers.IntegerField()                    # Serializer integer field representing the Movie's unique ID
    name = serializers.CharField()                    # Serializer character/string field for the movie's name
    description = serializers.CharField()                    # Serializer character/text field for the movie's description
    active = serializers.BooleanField()                    # Serializer boolean field representing active status

    def create(self, validated_data):                    # Method to create and return a new Movie instance using validated input
        return Movie.objects.create(**validated_data)                    # Performs database insert, creating Movie record, outputs Movie object

    def update(self, instance, validated_data):                    # Method to update and return an existing Movie instance using validated input
        instance.name = validated_data.get("name", instance.name)                    # Updates name attribute if provided, else retains original value.  If the user did not provide a new "name" in their API request, the dictionary .get() method defaults to the second argument: instance.name (the current database value).
                                                                                    
        instance.description = validated_data.get('description',instance.description)                    # Updates description attribute if provided, else retains original value

        instance.active = validated_data.get('active',instance.active)                    # Updates active attribute if provided, else retains original value

        instance.save()                    # Now Saves updated attributes of movie object to database. SQL has run

        return instance                    # Returns the updated Movie instance
    
    
    