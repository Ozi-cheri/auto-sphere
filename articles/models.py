from django.db import models
from cloudinary.models import CloudinaryField


class Article(models.Model):
    """
    Model representing an article with title, content, image, and votes.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def comment_count(self):
        """
        Returns the number of comments associated with the article.
        """
        return self.comments.count()


class Comment(models.Model):
    """
    Model representing a comment associated with an article.
    """
    article = models.ForeignKey(
        Article,
        related_name='comments',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.article.title}"

       