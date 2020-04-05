from django.db import models


class Book(models.Model):
    """Model definition for Book."""
    title = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        """Unicode representation of Book."""
        return self.title
