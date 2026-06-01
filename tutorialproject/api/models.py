from django.db import models                    # Imports models module containing Django DB field types

# Create your models here.


class BlogPost(models.Model):                    # Model class representing blog posts in the database
    title = models.CharField(max_length=100)                    # Character field to store the blog post's title (max length 100 characters)
    content = models.TextField()                    # Text field to store the main body content of the blog post
    published_date = models.DateTimeField(auto_now_add=True)                    # Datetime field set automatically to current date/time when created

    def __str__(self):                    # String representation function of this object
        return str(self.title)                    # Returns title string, representing instance in admin panels/logs
