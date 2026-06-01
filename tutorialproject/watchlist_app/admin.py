from django.contrib import admin                    # Imports Django admin module for site administration

from .models import Movie                    # Imports Movie model class from local models module

# Register your models here.
admin.site.register(Movie)                    # Registers Movie model on admin site to manage database records via GUI