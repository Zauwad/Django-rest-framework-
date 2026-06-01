from rest_framework.decorators import api_view                    # Imports api_view decorator to restrict allowed HTTP methods, outputs decorators namespace
from rest_framework.response import Response                    # Imports Response class, outputs Response class definition
from watchlist_app.api.serializers import MovieSerializer                    # Imports MovieSerializer, outputs serializer class definition
from watchlist_app.models import Movie                    # Imports Movie model, outputs Django model class definition
from rest_framework import status                    # Imports status module for HTTP status codes, outputs status namespace
from rest_framework.views import APIView                    # Imports APIView class for class-based views

# class-based API views using DRF's APIView for more structured handling of HTTP methods, validation, and responses.
class MovieListApiView(APIView):                    # Class-based API view for movie list and create operations, outputs a class definition
    def get(self, request):                    # Method handling GET requests for movie list, outputs/returns a Response object (E.g., <Response status_code=200, "application/json">)
        movies = Movie.objects.all()                    # Queries database for all Movie instances; outputs a QuerySet of Movie instances (E.g., <QuerySet [<Movie: Inception>]>)
        serializer = MovieSerializer(movies, many=True)                    # Instantiates MovieSerializer; outputs a MovieSerializer instance containing serialized movie list details (E.g., serializer.data: [{'id': 1, 'name': 'Inception', 'description': 'Dream heist', 'active': True}])
        return Response(serializer.data)                    # Instantiates and outputs/returns a Response object containing serialized movie list (status 200) (E.g., Response([{'id': 1, 'name': 'Inception', ...}]))

    def post(self, request):                    # Method handling POST requests for creating a new movie, outputs/returns a Response object (E.g., <Response status_code=201, "application/json">)
        serializer = MovieSerializer(data=request.data)                    # Instantiates serializer with request payload dict; outputs a MovieSerializer instance for validation (E.g., request.data: {'name': 'Cars
        if serializer.is_valid():                    # Validates fields against serializer definition rules; outputs/returns a boolean (E.g., True)
            serializer.save()                    # Triggers serializer create() method; saves new Movie to DB, outputs/returns the new Movie model instance (E.g., <Movie: Cars>)
            return Response(serializer.data, status=status.HTTP_201_CREATED)                    # Instantiates and outputs/returns a Response object containing serialized new movie dict with status 201 (E.g., Response({'id': 1, 'name': 'Cars', ...}))
        else:                    # Executes if validation fails
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)                    # Instantiates and outputs/returns a Response object containing validation errors dictionary with status 400 (E.g., Response({'name': ['This field is required.']}))




class MovieDetailsApiView(APIView):                    # Class-based API view for single movie operations, outputs a class definition
    def get(self, request, pk): 
        movie = Movie.objects.get(pk = pk)  #pk is the primary key passed in the URL, such as /movie/1/ where 1 is the primary key. If no such Movie exists, it will raise a DoesNotExist exception.
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def put(self, request, pk):
        movie = Movie.objects.get(pk = pk)
        serializer = MovieSerializer(movie, data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_304_NOT_MODIFIED)   

    def delete(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)







# Function-based API views using DRF features for more robust handling of HTTP methods, validation, and responses. Each view handles specific operations for Movie instances, utilizing MovieSerializer for data serialization and validation, and Response for consistent API responses.
# @api_view(['GET', 'POST'])                    # Limits endpoint to GET and POST methods, outputs decorated view callable function
# def movie_list(request):                    # API view handling GET (list) and POST (create), outputs/returns a Response object (E.g., <Response status_code=200, "application/json">)
#     if request.method == 'GET':                    # Checks HTTP request method, outputs/evaluates to a boolean (E.g., True)
#         movies = Movie.objects.all()                    # Queries database for all Movie instances; outputs a QuerySet of Movie instances (E.g., <QuerySet [<Movie: Inception>]>)
#         serializer = MovieSerializer(movies, many=True)                    # Instantiates MovieSerializer; outputs a MovieSerializer instance containing serialized movie list details (E.g., serializer.data: [{'id': 1, 'name': 'Inception', 'description': 'Dream heist', 'active': True}])
#         print("->",serializer.data)                    # Prints serializer.data (which outputs list of serialized movie dicts) to console, returns None (E.g., None)
#         return Response(serializer.data)                    # Instantiates and outputs/returns a Response object containing serialized movie list (status 200) (E.g., Response([{'id': 1, 'name': 'Inception', ...}]))

#     if request.method == 'POST':                    # Checks HTTP request method, outputs/evaluates to a boolean (E.g., True)
#         serializer = MovieSerializer(data=request.data)                    # Instantiates serializer with request payload dict; outputs a MovieSerializer instance for validation (E.g., request.data: {'name': 'Cars', 'description': 'Race car', 'active': True}) request.data changes json to dict, Response changes dict to json
#         if serializer.is_valid():                    # Validates fields against serializer definition rules; outputs/returns a boolean (E.g., True)
#             print("After post->",serializer)                    
#             serializer.save()                    # Triggers serializer create() method; saves new Movie to DB, outputs/returns the new Movie model instance (E.g., <Movie: Cars>)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)                    # Instantiates and outputs/returns a Response object containing serialized new movie dict (E.g., Response({'id': 1, 'name': 'Cars', ...}))
#         else:                    # Executes if validation fails
#             return Response(serializer.errors)                    # Instantiates and outputs/returns a Response object containing validation errors dictionary (E.g., Response({'name': ['This field is required.']}))
     



# @api_view(['GET', 'PUT', 'DELETE'])                    # Limits endpoint to GET, PUT, and DELETE methods, outputs decorated view callable (E.g., <function movie_details at 0x...>)
# def movie_details(request, pk):                    # API view for single movie operations, outputs/returns a Response object (E.g., <Response status_code=200, "application/json">)
#     try:                    # Begins lookup exception block, outputs control flow direction
#         movie = Movie.objects.get(pk=pk)                    # Queries DB for single movie matching pk; outputs a single Movie model instance (E.g., <Movie: Inception>)
#     except Movie.DoesNotExist:                    # Catches DoesNotExist exception if pk is missing, outputs exception instance
#         return Response({'Error': 'Movie not found'}, status=404)                    # Instantiates and outputs/returns a Response object with status 404 (E.g., Response({'Error': 'Movie not found'}))



#     if request.method == 'GET':                    # Checks HTTP request method, outputs/evaluates to a boolean (E.g., True)
#         serializer = MovieSerializer(movie)                    # Instantiates serializer with movie instance; outputs a MovieSerializer instance for single object (E.g., serializer.data: {'id': 1, 'name': 'Inception', 'description': 'Dream heist', 'active': True})
#         return Response(serializer.data)                    # Instantiates and outputs/returns a Response object containing the serialized movie dict (E.g., Response({'id': 1, 'name': 'Inception', ...}))

#     if request.method == 'PUT':                    # Checks HTTP request method, outputs/evaluates to a boolean (E.g., True)
#         serializer = MovieSerializer(movie, data=request.data)                     # Instantiates serializer with movie instance and new payload; outputs a MovieSerializer instance for update (E.g., request.data: {'name': 'Updated Movie', 'description': 'New desc', 'active': False})
#         if serializer.is_valid():                    # Validates updated fields; outputs/returns a boolean (E.g., True)
#             serializer.save()                    # Triggers serializer update() method; saves changes to DB, outputs/returns updated Movie model instance (E.g., <Movie: Updated Movie>)
#             return Response(serializer.data)                    # Instantiates and outputs/returns a Response object containing the serialized updated movie dict (E.g., Response({'id': 1, 'name': 'Updated Movie', ...}))
#         else:                    # Executes if validation fails
#             return Response(serializer.errors)                    # Instantiates and outputs/returns a Response object containing validation errors dictionary (E.g., Response({'name': ['This field is required.']}))

#     if request.method == 'DELETE':                    # Checks HTTP request method, outputs/evaluates to a boolean (E.g., True)
#         movie.delete()                    # Deletes movie record from DB; executes SQL deletion, outputs/returns a tuple containing rows affected (E.g., (1, {'watchlist_app.Movie': 1}))
#         return Response(status=204)                    # Instantiates and outputs/returns a Response object with status 204 (No Content) (E.g., Response(status=204))
