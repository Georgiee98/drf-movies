from django.db import models


class MovieData(models.Model):
    name = models.CharField(max_length=255)
    duration = models.FloatField()
    rating = models.FloatField()


    def __str__(self):
        return f"id: {self.id} - {self.name}"