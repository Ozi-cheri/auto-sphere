from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    """
    Admin customization for the Article model.
    """
    list_display = ('title', 'created_at', 'upvotes', 'downvotes')
    list_filter = ('created_at',)
    search_fields = ('title', 'content')


admin.site.register(Article, ArticleAdmin)