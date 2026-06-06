from django.db import models                    # Imports models module containing Django DB field types
from django.core.validators import MinValueValidator, MaxValueValidator
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
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='watchlist') # This field creates a foreign key relationship to the StreamPlatform model, allowing each Movie to be associated with one streaming platform. The on_delete=models.CASCADE argument ensures that if a StreamPlatform is deleted, all associated WatchList entries will also be deleted. The related_name='watchlist' allows reverse access from StreamPlatform to its related WatchList entries using stream_platform_instance.watchlist.
    
    def __str__(self):                    # String representation function of this object
        return str(self.title)                    # Returns movie name string, representing instance in admin panels/logs



class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) #Here auto_now updates the field every time the object is saved
    
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="reviews")