from django.shortcuts import render
from .models import Post
# Create your views here.

def home(request):
    posts = Post.objects.filter(is_available=True)
    return render(request, 'rental/home.html')