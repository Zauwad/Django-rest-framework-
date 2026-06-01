#This one is the old views file. It is not used in the project. It is only for reference to show how we can create API views without using DRF serializers and Response objects. The new views file (views.py) uses DRF features to create more robust and flexible API endpoints. 



from django.http import JsonResponse                    # Imports JsonResponse to return dictionary data as formatted JSON, outputs response class reference (E.g., <class 'django.http.response.JsonResponse'>)
from django.shortcuts import render
from rest_framework.decorators import api_view                    # Imports render helper function for HTML templates, outputs renderer callable (E.g., <function render at 0x...>)

from .models import Movie                    # Imports Movie model class from local models module, outputs Django model reference (E.g., <class 'watchlist_app.models.Movie'>)

# Create your views here.

#Function based view. (vanilla django way)
@api_view(['GET'])
def movie_list(request):                    # Function-based view handling HttpRequest; outputs/returns a JsonResponse object (E.g., <JsonResponse status_code=200, "application/json">)
    movies = Movie.objects.all()                    # Queries database; outputs a QuerySet containing all Movie model instances (E.g., <QuerySet [<Movie: cars 1>]>)
    # print(list(movies.values()))
    # print(movies) -> only quertyset. <QuerySet [<Movie: cars 1>]>
    # 
    # print(movies.values()) -> dictionary. <QuerySet [{'id': 1, 'name': 'cars 1', 'description': 'discrip1', 'active': True}]>
    # 
    # print(list(movies.values()))
    # [{'id': 1, 'name': 'cars 1', 'description': 'discrip1', 'active': True}]
    data = {                    # Dictionary mapping result payload keys, outputs a dictionary object (E.g., {'movies': [...]})
        "movies" : list(movies.values())                    # Evaluates database fields; list() outputs a list containing movie dictionaries (E.g., [{'id': 1, 'name': 'cars 1', 'description': 'discrip1', 'active': True}])
    }                    # Closes data dictionary definition

    return JsonResponse(data)                    # Instantiates and returns JsonResponse; outputs a JsonResponse object with status 200 (E.g., JsonResponse({'movies': [...]}))


@api_view(['GET'])
def movie_details(request, pk):                    # Function-based view handling single movie detail request; outputs/returns a JsonResponse object (E.g., <JsonResponse status_code=200, "application/json">)
    movie = Movie.objects.get(pk=pk)                    # Queries single movie matching pk; outputs a single Movie model instance (E.g., <Movie: cars 1>)
    data = {                    # Dictionary holding attributes of single movie, outputs a dictionary object (E.g., {'name': 'cars 1', 'description': 'discrip1', 'active': True})
        'name': movie.name,                    # Reads name field of the movie instance; outputs a string (E.g., 'cars 1')
        'description': movie.description,                    # Reads description field of the movie instance; outputs a text string (E.g., 'discrip1')
        'active': movie.active                    # Reads active status field of the movie instance; outputs a boolean (E.g., True)
    }                    # Closes data dictionary definition

    return JsonResponse(data)                    # Instantiates and returns JsonResponse; outputs a JsonResponse object containing single movie attributes (E.g., JsonResponse({'name': 'cars 1', ...}))