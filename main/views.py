import django.contrib.auth
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Post, Book, Comment, Profile
from .forms import PostForm
from django.contrib.auth.models import  User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    # This is for the search filters
    posts = Post.objects.filter(
        Q(Book__title__icontains=q) |
        Q(title__icontains=q) |
        Q(content__icontains=q)
    )
    books = Book.objects.all()
    post_count = posts.count()
    context = {'posts': posts, 'books' : books, 'post_count': post_count }
    return render(request, 'main/home.html', context)

def post(request, pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=pk)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        comment = Comment.objects.create(
            author = request.user.profile,
            post = post,
            content = request.POST.get('content')
        )
        return redirect('post', pk=post.id)
    context = {'post': post, 'comments': comments}
    return render(request, 'main/post.html', context)

@login_required(login_url='/login')
def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.profile
            post.save()
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

@login_required(login_url='/login')
def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.user != post.author:
        return HttpResponse('You are  not allowed here!')

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'post': post, 'form': form}
    return render(request, 'main/post_form.html', context)

@login_required(login_url='/login')
def deletePost(request,pk):
    post = Post.objects.get(id=pk)

    if request.user != post.author:
        return HttpResponse('You are  not allowed here!')

    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'main/delete.html', {'obj': post})


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
           user = User.objects.get(username=username)
        except:
            messages.error(request, 'User with this username does not exist')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is does not exist')

    context = {'page': page}
    return render(request, 'main/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')

    context = {'form': form}
    return render(request, 'main/login_register.html', context)
