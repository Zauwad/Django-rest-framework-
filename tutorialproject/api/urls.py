from django.urls import path                    # Imports path function to define individual URL patterns

from . import views                    # Imports local views module to hook views to route endpoints

urlpatterns = [                    # Defines localized URL pattern mappings for the blogpost api
    path("blogposts/", views.BlogPostListCreate.as_view(), name="blogpost-view-create"),                    # Maps 'blogposts/' to list/create view class, outputs JSON response
    path(                    # Multi-line path registration function
        "blogposts/<int:pk>/",                    # URL pattern capturing integer primary key parameter
        views.BlogPostRetrieveUpdateDestroy.as_view(),                    # Binds URL matching pk to retrieve/update/destroy view
        name="update-distroy",                    # Name identifier for this endpoint route
    ),                    # Closes path registration
]                    # Ends api urlpatterns list
