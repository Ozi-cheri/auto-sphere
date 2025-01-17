from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Article, Comment
from .forms import CommentForm


def home_view(request):
    return render(request, 'articles/home.html')


def signup_view(request):
    return render(request, 'signup.html')


def login_view(request):
    return render(request, 'login.html')


def articles_view(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'articles/articles.html', {'page_obj': page_obj})


def upvote_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.upvotes += 1
    article.save()
    return redirect('articles')


def downvote_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.downvotes += 1
    article.save()
    return redirect('articles')


def article_detail_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments.all()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('article_detail', pk=pk)
    else:
        form = CommentForm()

    return render(request, 'articles/article_detail.html', {
        'article': article,
        'comments': comments,
        'form': form,
    })
