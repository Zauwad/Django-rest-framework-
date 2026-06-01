from django.urls import  path                    # Imports path function to define individual URL patterns
# from .views import movie_details, movie_list                    # Imports details and list views from local views module
from .views import MovieListApiView, MovieDetailsApiView


urlpatterns = [                    # List mapping movie URLs to their respective views (API routes)
    path('lists/', MovieListApiView.as_view(), name = "movie-list"),                    # Maps 'lists/' path to movie_list view function, outputs JSON response
    path('lists/<int:pk>', MovieDetailsApiView.as_view(), name='movie-details')                    # Maps 'lists/<pk>' detail URL path to movie_details view function, outputs JSON response
]                    # Ends urlpatterns list

# 26-> mysite.com/hello
# path('todos/', include(todos.urls) -> mysite.com/todos/hello
