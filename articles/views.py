from django.shortcuts import render

# Create your views here.

def home(request):
    """
    View function for the Home Page.
    Renders the 'home.html' template.
    """
    return render(request, 'home.html')