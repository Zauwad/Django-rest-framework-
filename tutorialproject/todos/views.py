from django.shortcuts import render                    # Imports render function to compile HTML templates with context, outputs response rendering callable (E.g., <function render at 0x...>)
from django.http import HttpResponse                    # Imports HttpResponse class to return raw HTTP/text payloads, outputs response class reference (E.g., <class 'django.http.response.HttpResponse'>)

# this one is for routing or endpoints. We can define our views here, which will handle the logic for processing requests and returning responses. Views are responsible for fetching data from the database, processing it, and rendering templates to display the data to the user. By defining our views in this file, we can easily manage the flow of our application and create dynamic web pages based on user interactions.
#request response
# Create your views here.
def hello_world_view(request):                    # Request processing function; receives HttpRequest, outputs/returns HttpResponse object (E.g., <HttpResponse status_code=200, "text/html">)
    return HttpResponse('Hello World')                    # Instantiates and returns HttpResponse; outputs HttpResponse containing plain text 'Hello World' (E.g., HttpResponse("Hello World"))


def hello_python_view(request):                    # Request processing function; receives HttpRequest, outputs/returns HttpResponse object (E.g., <HttpResponse status_code=200, "text/html">)
    return HttpResponse('Hello Python!')                    # Instantiates and returns HttpResponse; outputs HttpResponse containing plain text 'Hello Python!' (E.g., HttpResponse("Hello Python!"))

def hello_html_view(request):                    # Request processing function; receives HttpRequest, outputs/returns HttpResponse object (E.g., <HttpResponse status_code=200, "text/html">)
    return render(request, 'todos/hello.html')                    # Compiles and returns template payload; outputs HttpResponse rendering template file (E.g., HttpResponse("<html>hello</html>"))