from django.db import models                    # Imports models module containing Django DB field types

# Create your models here.


class Movie(models.Model):                    # Model class representing Movie records in the database
    name = models.CharField(max_length=50)                    # Character field to store the movie name (max length 50)
    description = models.TextField(max_length=200)                    # Text field to store movie description (max length 200)
    active = models.BooleanField(default=True)                    # Boolean field tracking if movie is active/available, defaults to True

    def __str__(self):                    # String representation function of this object
        return str(self.name)                    # Returns movie name string, representing instance in admin panels/logs
