from django.db import models

class MovieElement(models.Model):
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    definition = models.TextField()
    example = models.URLField(null=True, blank=True, default =" ")
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name
