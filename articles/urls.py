from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  
    path('signup/', views.signup_view, name='signup'),  
    path('login/', views.login_view, name='login'),
    path('articles/', views.articles_view, name='articles'),
    path('articles/<int:article_id>/upvote/', views.upvote_article, name='upvote_article'),  
    path('articles/<int:article_id>/downvote/', views.downvote_article, name='downvote_article'),  
    path('articles/<int:pk>/', views.article_detail_view, name='article_detail'), 
    
    
]
