from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Article

# Home View: Displays the welcome message
def home_view(request):
    return render(request, 'articles/home.html')  # Updated to point to 'articles/home.html'

# Sign Up View
def signup_view(request):
    return render(request, 'signup.html')

# Login View
def login_view(request):
    return render(request, 'login.html')  

# Articles View: Displays articles with pagination
def articles_view(request):  
    articles = Article.objects.all()
    paginator = Paginator(articles, 5)  # 5 articles per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 
    return render(request, 'articles/articles.html', {'page_obj': page_obj})
