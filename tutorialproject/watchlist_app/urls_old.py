from django.urls import  path                    # Imports path function to define individual URL patterns
from .views_old import movie_details, movie_list                    # Imports details and list views from local views_old module
# include is used to use other routing from other apps

urlpatterns = [                    # List mapping movie URLs to their respective views (old vanilla django routes)
    path('lists/', movie_list, name = "movie-list"),                    # Maps 'lists/' path to movie_list view function, outputs JSON response
    path('lists/<int:pk>', movie_details, name='movie-details')                    # Maps 'lists/<pk>' detail URL path to movie_details view function, outputs JSON response
]                    # Ends old urlpatterns list

# 26-> mysite.com/hello
# path('todos/', include(todos.urls) -> mysite.com/todos/hello
