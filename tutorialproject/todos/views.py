from django.shortcuts import render
from django.http import HttpResponse

# this one is for routing or endpoints. We can define our views here, which will handle the logic for processing requests and returning responses. Views are responsible for fetching data from the database, processing it, and rendering templates to display the data to the user. By defining our views in this file, we can easily manage the flow of our application and create dynamic web pages based on user interactions.
#request response
# Create your views here.
def hello_world_view(request):
    return HttpResponse('Hello World')


def hello_python_view(request):
    return HttpResponse('Hello Python!')

def hello_html_view(request):
    return render(request, 'todos/hello.html')