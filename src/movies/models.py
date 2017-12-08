from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True) # optional

    def __str__(self):
        """
        Devuelve la representación del objeto en string
        """
        return self.name

class Movie(models.Model):

    name = models.CharField(max_length=150)
    summary = models.TextField()
    director_name = models.CharField(max_length=100)
    release_date = models.DateField()
    image = models.URLField()
    rating = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Devuelve la representación del objeto en string
        """
        return self.name