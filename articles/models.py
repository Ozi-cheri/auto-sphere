from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Article(models.Model):
    """
    Model representing an article with title, content, image, and votes.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    upvotes = models.PositiveIntegerField(default=0)
    downvotes = models.PositiveIntegerField(default=0)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='articles'
    )

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
        'Article',
        related_name='comments',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        related_name='comments',
        on_delete=models.CASCADE
    )
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.article.title}"
