from django.urls import path                    # Imports path function to define individual URL patterns
from . import views                    # Imports local views module to hook views to route endpoints

# Here main routing happens, 

urlpatterns = [                    # Defines URL configurations mapping endpoints to view actions for todos application
    path('hello/', views.hello_world_view, name='hello_world'),                    # Routes 'hello/' URL to hello_world_view, returns plain Hello World text
    path('', views.hello_python_view, name= 'hello_python' ),                    # Routes root URL of app to hello_python_view, returns plain Hello Python text
    path('html/', views.hello_html_view, name='html_rende')                    # Routes 'html/' URL to hello_html_view, renders HTML template
]                    # Ends urlpatterns definition list
    # after this have to import these urls to core apps urlywc