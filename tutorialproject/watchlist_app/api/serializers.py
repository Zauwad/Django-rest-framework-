from rest_framework import serializers, validators                    # Imports DRF serializers to convert model instances to/from JSON
from watchlist_app.models import Movie                    # Imports Movie model class from local watchlist_app models

#BELOW IS THE SERIALIZERS.MODELSERIALIZER CLASS FOR MOVIE MODEL. THIS CLASS AUTOMATICALLY GENERATES FIELDS BASED ON THE MOVIE MODEL, AND ALSO INCLUDES BASIC VALIDATION LOGIC. IT IS A MORE CONCISE WAY TO DEFINE A SERIALIZER WHEN YOU WANT TO USE ALL OR MOST OF THE MODEL FIELDS WITHOUT CUSTOM VALIDATION LOGIC.
#IT HAS CREATE AND UPDATE METHODS BUILT IN, SO YOU DONT NEED TO DEFINE THEM UNLESS YOU WANT TO OVERRIDE THE DEFAULT BEHAVIOR. IT ALSO AUTOMATICALLY HANDLES THE CREATION OF NEW MOVIE INSTANCES AND UPDATING EXISTING ONES BASED ON THE MODEL FIELDS, WITHOUT REQUIRING EXPLICIT CREATE/UPDATE METHODS UNLESS CUSTOM LOGIC IS NEEDED.
class MovieSerializer(serializers.ModelSerializer):                    # Serializer class for Movie model, using DRF's ModelSerializer for automatic field generation
    class Meta:
        model = Movie
        fields = "__all__"
        # fields = ['id', 'name', 'description']  # Explicitly specifying fields to include in the serializer output (id, name, description). Wont show 'active' field in API responses.
        #exclude = ['name'] # Exclude the "name" field from the API responses. However, it can still be used for input when creating/updating Movie instances through the API.
    
    len_name = serializers.SerializerMethodField() #This adds a custom read-only field to the serializer output that calculates the length of the "name" field for each Movie instance. The value of this field is determined by the get_len_name method defined below. It will be included in the API responses as an additional field alongside the model fields.
    def get_len_name(self, object):
        return len(object.name)
    
    
    def validate_name(self, value):                   
        if len(value) < 2:
            raise serializers.ValidationError("name too short ")
        else:
            return value

    def validate(self, data):   
        if data["name"] == data["description"]:
            raise serializers.ValidationError("name And description has to be different!!")
        else:
            return data
            
















#BELOW IS THE SERIALIZERS.SERIALIZER CLASS FOR MOVIE MODEL. THIS CLASS DEFINES HOW MOVIE INSTANCES ARE CONVERTED TO/FROM JSON, AND ALSO INCLUDES VALIDATION LOGIC FOR THE FIELDS.
# def description_length(value):
#     if len(value) < 10:
#         raise serializers.ValidationError("Description too small!!")

# class MovieSerializer(serializers.Serializer):                    # Serializer class defining fields and validation logic for Movie instances
#     id = serializers.IntegerField(read_only=True)       #Here read_only is core argument                   # Serializer integer field representing the Movie's unique ID
#     name = serializers.CharField()                    # Serializer character/string field for the movie's name
#     #Below one is validators type validation. 
#     description = serializers.CharField(validators=[description_length])                    # Serializer character/text field for the movie's description
#     active = serializers.BooleanField()                    # Serializer boolean field representing active status


#     #field-level validation method for the "name" field. This method is automatically called by DRF during validation of the serializer, and it checks the validity of the "name" field specifically.
#     def validate_name(self, value):                     #value is the name field value that the user has provided in their API request. 
#         if len(value) < 2:
#             raise serializers.ValidationError("name too short ")
#         else:
#             return value

#     #Object level Validation method for the entire Movie object. This method is automatically called by DRF during validation of the serializer, and it checks the validity of the entire object (all fields together).
#     def validate(self, data):  # data will come here as a dictionary of all the fields and their values that the user has provided in their API request. 
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError("name And description has to be different!!")
#         else:
#             return data
    

#     #These below starts sql after serializer.save() in views
#     def create(self, validated_data):                    # Method to create and return a new Movie instance using validated input. validated_data comes from views after it gets validated by .isValid() method
#         return Movie.objects.create(**validated_data)                    # Performs database insert, creating Movie record, outputs Movie object

#     def update(self, instance, validated_data):                    # Method to update and return an existing Movie instance using validated input
#         instance.name = validated_data.get("name", instance.name)                    # Updates name attribute if provided, else retains original value.  If the user did not provide a new "name" in their API request, the dictionary .get() method defaults to the second argument: instance.name (the current database value).
                                                                                    
#         instance.description = validated_data.get('description',instance.description)                    # Updates description attribute if provided, else retains original value

#         instance.active = validated_data.get('active',instance.active)                    # Updates active attribute if provided, else retains original value

#         instance.save()                    # Now Saves updated attributes of movie object to database. SQL has run

#         return instance                    # Returns the updated Movie instance
    
    
    