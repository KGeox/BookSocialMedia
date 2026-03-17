from django.shortcuts import render, redirect
from .models import Post, Book, Comment, Profile
from .forms import PostForm

# Create your views here.

def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'main/home.html', context)

def post(request, pk):
    post = Post.objects.get(id=pk)
    comment = Comment.objects.filter(post=pk)
    context = {'post': post, 'comment': comment}
    return render(request, 'main/post.html', context)

def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'main/post_form.html', context)

def about(request):
    return render(request, 'main/about.html')

def profile(request):
    posts = Post.objects.filter(author=request.user)
    context = {'posts': posts}
    return render(request, 'main/profile.html', context)

def book(request, pk):
    book =Book.objects.get(id=pk)
    context = {'book': book}
    return render(request, 'main/book.html', context)

def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'post': post, 'form': form}
    return render(request, 'main/post_form.html', context)