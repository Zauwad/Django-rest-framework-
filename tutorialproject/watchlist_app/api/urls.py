from django.urls import  path
from .views import movie_details, movie_list
# include is used to use other routing from other apps

urlpatterns = [
    path('lists/', movie_list, name = "movie-list"),
    path('lists/<int:pk>', movie_details, name='movie-details')
]

# 26-> mysite.com/hello
# path('todos/', include(todos.urls) -> mysite.com/todos/hello
