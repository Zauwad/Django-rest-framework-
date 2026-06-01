"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# This one is for routing

from django.contrib import admin                    # Imports admin module, outputs admin registration namespace
from django.urls import include, path                    # Imports route helpers, outputs include and path callable functions

urlpatterns = [                    # Declares list of URLResolver/URLPattern elements, outputs a list object containing route definitions
    path('admin/', admin.site.urls),                    # Configures admin routes, path() outputs a URLPattern object
    path('', include('todos.urls')),                    # Nesting todos URLs: include() outputs nested route tuple; path() outputs a URLResolver object
    path('', include('api.urls')),                    # Nesting api URLs: include() outputs nested route tuple; path() outputs a URLResolver object
    path('movie/', include('watchlist_app.api.urls'))                    # Nesting movie API: include() outputs nested route tuple; path() outputs a URLResolver object
]                    # Ends declaration of urlpatterns list

# 26-> mysite.com/hello
# path('todos/', include(todos.urls) -> mysite.com/todos/hello
