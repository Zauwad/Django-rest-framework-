from django.urls import  path                    # Imports path function to define individual URL patterns
# from .views import movie_details, movie_list                    # Imports details and list views from local views module
from .views import WatchListApiView, WatchDetailsApiView, StreamPlatformApiView, StreamPlatformDetailsApiView


urlpatterns = [                    # List mapping movie URLs to their respective views (API routes)
    path('watchlists/', WatchListApiView.as_view(), name = "WatchList-list"),                    # Maps 'lists/' path to movie_list view function, outputs JSON response
    path('watchlists/<int:pk>', WatchDetailsApiView.as_view(), name='WatchList-detail'),                    # Maps 'lists/<pk>' detail URL path to movie_details view function, outputs JSON response
    path('platforms/', StreamPlatformApiView.as_view(), name="streamplatform-list"),        # The name argument in the path function is used to give a unique identifier to each URL pattern. This allows you to refer to these URL patterns by name elsewhere in your code (e.g., in serializers, templates, or when reversing URLs) instead of hardcoding the URL paths. By using named URL patterns, you can easily change the actual URL structure in the future without having to update all references to those URLs throughout your codebase, as you can simply refer to them by their names. In this case, "streamplatform-list" and "streamplatform-detail" are the names given to the list and detail views for the StreamPlatform model, respectively.
    path('platforms/<int:pk>', StreamPlatformDetailsApiView.as_view(), name="streamplatform-detail"),  # It is common to use a naming convention that includes the model name and the type of view (e.g., list, detail) to ensure uniqueness and clarity when referring to these URL patterns elsewhere in the code. This is needed for reverse URL lookups, such as when using HyperlinkedRelatedField in serializers to generate hyperlinks to related objects. By providing a name for each URL pattern, you can easily reference these patterns by name instead of hardcoding the URL paths, which improves maintainability and flexibility in your codebase.
    
]                    # Ends urlpatterns list

# 26-> mysite.com/hello
# path('todos/', include(todos.urls) -> mysite.com/todos/hello
