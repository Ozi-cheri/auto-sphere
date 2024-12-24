from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Article

# Create your views here.

def home_view(request):
    articles = Article.objects.all().order_by('-published_date')
    paginator = Paginator(articles, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number) 
    return render(request, 'articles/home.html', {'page_obj': page_obj})  