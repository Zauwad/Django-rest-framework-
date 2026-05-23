from django.shortcuts import render  
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import BlogPost
from .serializers import BlogPostSerializer


# Create your views here.
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    # custom function
    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"



# Overriding generics
class BlogPostListByTitle(APIView):
    def get(self, request, format = None):
        # getting title from query parameter
        title = request.query_params.get("title", "")

        if title:
            #filtering based on title
            blog_posts_byTitle = BlogPost.objects.filter(title__icontains=title)
        else:
            blog_posts = BlogPost.objects.all()

        serializer = BlogPostSerializer(blog_posts, many=True) #Converting to json
        return Response(serializer.data, status = status.HTTP_200_OK)