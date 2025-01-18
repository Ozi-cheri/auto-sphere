from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from .models import Article, Comment
from .forms import CommentForm


def home_view(request):
    return render(request, 'articles/home.html')


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            messages.success(request, "Account created successfully. You are now logged in.")
            return redirect('home')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def articles_view(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'articles/articles.html', {'page_obj': page_obj})


@login_required
def upvote_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.upvotes += 1
    article.save()
    messages.success(request, "You upvoted this article.")
    return redirect('articles')


@login_required
def downvote_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.downvotes += 1
    article.save()
    messages.success(request, "You downvoted this article.")
    return redirect('articles')


def article_detail_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments.all()

    if request.method == "POST":
        if request.user.is_authenticated:  
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.article = article
                comment.author = request.user  
                comment.save()
                messages.success(request, "Comment added successfully.")
                return redirect('article_detail', pk=pk)
        else:
            messages.error(request, "You must log in to add a comment.")
            return redirect('login')
    else:
        form = CommentForm()

    return render(request, 'articles/article_detail.html', {
        'article': article,
        'comments': comments,
        'form': form,
    })


@login_required
def delete_comment(request, comment_id):
    # Get the comment, or return 404 if not found
    comment = get_object_or_404(Comment, id=comment_id)

    # Ensure that the user trying to delete the comment is the author
    if comment.author == request.user:
        comment.delete()
        messages.success(request, "Comment deleted successfully.")
    else:
        messages.error(request, "You can only delete your own comments.")

    # Redirect back to the article detail page
    return redirect('article_detail', pk=comment.article.id)
