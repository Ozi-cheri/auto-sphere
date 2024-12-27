from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Article

# Create your views here.

def home_view(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 
    return render(request, 'articles/home.html', {'articles': articles})  

def signup_view(request):
    return render(request, 'signup.html')

def login_view(request):
    return render(request, 'login.html')  

def articles_view(request):  
    articles = Article.objects.all()
    return render(request, 'articles/articles.html', {'articles': articles})    