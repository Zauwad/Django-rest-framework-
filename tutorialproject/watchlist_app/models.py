from django.db import models                    # Imports models module containing Django DB field types

# Create your models here.


class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)

    def __str__(self):
        return str(self.name)


class WatchList(models.Model):                    # Model class representing Movie records in the database
    title = models.CharField(max_length=50)                    # Character field to store the movie name (max length 50)
    storyline = models.TextField(max_length=200)                    # Text field to store movie description (max length 200)
    active = models.BooleanField(default=True)                    # Boolean field tracking if movie is active/available, defaults to True
    created = models.DateTimeField(auto_now_add=True)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='watchlist')
    
    def __str__(self):                    # String representation function of this object
        return str(self.title)                    # Returns movie name string, representing instance in admin panels/logs
