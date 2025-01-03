from django.contrib import admin

# Register your models here.

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'upvotes', 'downvotes')  
    list_filter = ('created_at',)  
    search_fields = ('title', 'content') 

admin.site.register(Article, ArticleAdmin)
