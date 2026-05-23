from django.apps import AppConfig

# basic configuration for the 'todos' app. It defines the name of the app, which is used by Django to identify it and include it in the project. This file is necessary for Django to recognize the app and its components, such as models, views, and templates.
# Have to add this app to main core settings.py

class TodosConfig(AppConfig):
    name = 'todos'
