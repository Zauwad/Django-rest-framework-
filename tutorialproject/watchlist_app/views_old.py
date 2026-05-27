from django.http import JsonResponse
from django.shortcuts import render

from .models import Movie

# Create your views here.

#Function based view. (vanilla django way)
def movie_list(request):
    movies = Movie.objects.all()
    print(list(movies.values()))
    # print(movies) -> only quertyset. <QuerySet [<Movie: cars 1>]>
    # 
    # print(movies.values()) -> dictionary. <QuerySet [{'id': 1, 'name': 'cars 1', 'description': 'discrip1', 'active': True}]>
    # 
    # print(list(movies.values()))
    # [{'id': 1, 'name': 'cars 1', 'description': 'discrip1', 'active': True}]
    data = {
        "movies" : list(movies.values())
    } 

    return JsonResponse(data)



def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        'name': movie.name,
        'description': movie.description,
        'active': movie.active
    }

    return JsonResponse(data)
    