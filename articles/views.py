from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from .models import Article, Comment
from .forms import CommentForm
from .models import Article
from .forms import ArticleForm



def home_view(request):
    return render(request, 'articles/home.html')

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully. You are now logged in.")
            return redirect('articles')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})

def login_view(request):
    next_url = request.GET.get('next', 'articles')
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect(next_url)
        messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def articles_view(request):
    articles = Article.objects.all().order_by('-created_at')  
    paginator = Paginator(articles, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'articles/articles.html', {'page_obj': page_obj})

@login_required(login_url='/signup/')
def upvote_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.upvotes += 1
    article.save()
    return redirect('articles')

@login_required(login_url='/signup/')
def downvote_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.downvotes += 1
    article.save()
    return redirect('articles')

def article_detail_view(request, id):
    article = get_object_or_404(Article, id=id)
    comments = article.comments.all()

    return render(request, 'articles/article_detail.html', {
        'article': article,
        'comments': comments,
    })

@login_required
def add_comment(request, id):
    """
    Handles comment submission for an article.
    """
    article = get_object_or_404(Article, id=id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            messages.success(request, "Your comment has been posted!")
        else:
            messages.error(request, "There was an error with your comment.")

    return redirect('article_detail', id=id)


@login_required
def edit_comment(request, id):
    comment = get_object_or_404(Comment, id=id)

    
    if request.user != comment.user:
        messages.error(request, "You are not allowed to edit this comment.")
        return redirect("article_detail", id=comment.article.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, "Comment updated successfully.")
        else:
            messages.error(request, "Failed to update the comment. Please try again.")

    return redirect("article_detail", id=comment.article.id)

@login_required
def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)

    
    if request.user != comment.user:
        messages.error(request, "You are not allowed to delete this comment.")
        return redirect("article_detail", id=comment.article.id)

    comment.delete()
    messages.success(request, "Comment deleted successfully.")
    return redirect("article_detail", id=comment.article.id)


def logout_confirm_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')
    return render(request, 'logout_confirm.html')



@login_required(login_url='/login/')
def create_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)  # 
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user  
            article.save()
            return redirect('articles')  
    else:
        form = ArticleForm()

    return render(request, 'create_article.html', {'form': form})   