from django.urls import path
from . import views

# Here main routing happens, 

urlpatterns = [
    path('hello/', views.hello_world_view, name='hello_world'),
    path('', views.hello_python_view, name= 'hello_python' ),
    path('html/', views.hello_html_view, name='html_rende')
]
    # after this have to import these urls to core apps urlywc