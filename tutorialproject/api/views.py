from django.shortcuts import render                    # Imports render helper function, outputs template response renderer callable
from rest_framework import generics, status                    # Imports DRF generic views and HTTP status codes namespace
from rest_framework.response import Response                    # Imports Response class definition
from rest_framework.views import APIView                    # Imports APIView base class, outputs APIView class reference
from django.shortcuts import render                    # Imports render helper function, outputs template response renderer callable (E.g., <function render at 0x000001>)
from rest_framework import generics, status                    # Imports DRF generic views and HTTP status codes namespace (E.g., <module 'rest_framework.status'>)
from rest_framework.response import Response                    # Imports Response class definition (E.g., <class 'rest_framework.response.Response'>)
from rest_framework.views import APIView                    # Imports APIView base class, outputs APIView class reference (E.g., <class 'rest_framework.views.APIView'>)

from .models import BlogPost                    # Imports BlogPost model class definition (E.g., <class 'api.models.BlogPost'>)
from .serializers import BlogPostSerializer                    # Imports BlogPostSerializer class definition (E.g., <class 'api.serializers.BlogPostSerializer'>)


# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):                    # Generic class-based view for listing and creating BlogPosts (E.g., <class 'api.views.BlogPostListCreate'>)
    queryset = BlogPost.objects.all()                    # Defines default database query; outputs a QuerySet of all BlogPost instances (E.g., <QuerySet [<BlogPost: My Title>]>)
    serializer_class = BlogPostSerializer                    # Declares serializer class used for validation/formatting; outputs a BlogPostSerializer class reference (E.g., <class 'api.serializers.BlogPostSerializer'>)

    # custom function
    def delete(self, request, *args, **kwargs):                    # Custom DELETE request handler to clear database, outputs a Response object (E.g., <Response status_code=204>)
        BlogPost.objects.all().delete()                    # Deletes all BlogPost instances from DB; executes SQL deletion, outputs a tuple of deletion stats (E.g., (2, {'api.BlogPost': 2}))
        return Response(status = status.HTTP_204_NO_CONTENT)                    # Instantiates and returns Response; outputs a Response object with status 204 (E.g., Response(status=204))

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):                    # Generic view for fetching, updating or deleting a single BlogPost (E.g., <class 'api.views.BlogPostRetrieveUpdateDestroy'>)
    queryset = BlogPost.objects.all()                    # Defines default database query for single retrieval; outputs a QuerySet of all BlogPost instances (E.g., <QuerySet [<BlogPost: My Title>]>)
    serializer_class = BlogPostSerializer                    # Declares serializer class used for validation/formatting; outputs a BlogPostSerializer class reference (E.g., <class 'api.serializers.BlogPostSerializer'>)
    lookup_field = "pk"                    # Sets lookup DB key attribute; outputs string 'pk' to map against captured route parameters (E.g., 'pk')



# Overriding generics
class BlogPostListByTitle(APIView):                    # Custom API view class to list BlogPosts filtered by title query parameter (E.g., <class 'api.views.BlogPostListByTitle'>)
    def get(self, request, format = None):                    # GET request handler mapping GET requests, outputs/returns a Response object (E.g., <Response status_code=200>)
        # getting title from query parameter
        title = request.query_params.get("title", "")                    # Retrieves query parameter 'title'; outputs string value (E.g., 'Inception')

        if title:                    # Checks if title parameter has a non-empty value, outputs/evaluates to boolean (E.g., True)
            #filtering based on title
            blog_posts = BlogPost.objects.filter(title__icontains=title)                    # Queries DB for matching posts; outputs a filtered QuerySet of BlogPost instances (E.g., <QuerySet [<BlogPost: Title>]>)
        else:                    # Executes if no query parameter is provided
            blog_posts = BlogPost.objects.all()                    # Queries DB for all posts; outputs a QuerySet of all BlogPost objects (E.g., <QuerySet [<BlogPost: Title>]>)

        serializer = BlogPostSerializer(blog_posts, many=True)                    # Instantiates serializer; outputs a BlogPostSerializer instance containing serialized post details (E.g., serializer.data: [{'id': 1, 'title': 'First Post', 'content': 'Hello', 'published_date': '2026-05-29T12:00:00Z'}])
        return Response(serializer.data, status = status.HTTP_200_OK)                    # Instantiates and returns Response; outputs Response object with serialized posts data (status 200) (E.g., Response([{'id': 1, ...}]))
