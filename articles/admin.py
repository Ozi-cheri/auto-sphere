from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    """
    Admin customization for the Article model.
    """
    list_display = ('title', 'created_at', 'published_date', 'upvotes', 'downvotes')  
    list_filter = ('created_at', 'published_date')  
    search_fields = ('title', 'content')
    fields = ('title', 'content', 'image', 'published_date', 'user')  
admin.site.register(Article, ArticleAdmin)
