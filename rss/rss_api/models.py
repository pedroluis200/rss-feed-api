# Create your models here.
from django.db import models

# Modelo para almacenar los feeds RSS
class RSSFeed(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    description = models.TextField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

# Modelo para almacenar los feeds seleccionados para publicar en Twitter
class SelectedFeed(models.Model):
    rss_feed = models.ForeignKey(RSSFeed, on_delete=models.CASCADE)
    selected = models.BooleanField(default=False)
    # Agrega otros campos relacionados con la publicación en Twitter si es necesario

    def __str__(self):
        return f'Selected Feed: {self.rss_feed.title}'
