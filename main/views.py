import django.contrib.auth
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from .models import Post, Book, Comment, Profile, BookClub
from .forms import PostForm, BookForm, ProfileForm, UserForm, BookClubForm
from django.contrib.auth.models import  User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    genre = request.GET.get('genre', '')
    # This is for the search filters
    posts = Post.objects.filter(
        Q(Book__title__icontains=q) |
        Q(title__icontains=q) |
        Q(content__icontains=q),
        Book__valid=True
    )

    if  genre:
        posts = posts.filter(Book__genre=genre)

    books = Book.objects.filter(valid=True)
    clubs = BookClub.objects.all()[:5]
    post_count = posts.count()
    post_comments = Comment.objects.filter(
        Q(post__Book__title__icontains=q)
    )

    genre_choices = Book.GENRE_CHOICES

    context = {'posts': posts,
               'books' : books,
               'post_count': post_count,
               'post_comments': post_comments,
               'clubs': clubs,
               'genre_choices': genre_choices,
               'selected_genre': genre,
               'current_q': q,
    }
    return render(request, 'main/home.html', context)

def post(request, pk):
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=pk).order_by('-date')

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
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.profile
            post.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'main/post_form.html', context)

def about(request):
    return render(request, 'main/about.html')

def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    posts = profile.post_set.all()
    post_comments = profile.comment_set.all()
    books = Book.objects.filter(post__author=profile, valid=True)
    clubs = BookClub.objects.all()
    context = {'posts': posts, 'profile': profile, 'post_comments': post_comments, 'books': books, 'clubs': clubs, 'genre_choices': Book.GENRE_CHOICES,  'selected_genre': '', 'current_q': '',}
    return render(request, 'main/profile.html', context)

def book(request, pk):
    book =Book.objects.get(id=pk)
    posts = book.post_set.all()
    clubs = BookClub.objects.all()
    context = {'book': book, 'posts': posts, 'clubs': clubs, 'genre_choices': Book.GENRE_CHOICES, 'selected_genre': '', 'current_q': '', 'books': Book.objects.filter(valid=True) }
    return render(request, 'main/book.html', context)

@login_required(login_url='/login')
def updatePost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.user != post.author.user:
        return HttpResponse('You are  not allowed here!')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'post': post, 'form': form}
    return render(request, 'main/post_form.html', context)

@login_required(login_url='/login')
def deletePost(request,pk):
    post = Post.objects.get(id=pk)

    if request.user != post.author.user:
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
            return render(request, 'main/login_register.html', {'page': page})

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

@login_required(login_url='/login')
def deleteComment(request,pk):
    comment = Comment.objects.get(id=pk)

    if request.user != comment.author.user:
        return HttpResponse('You are  not allowed here!')

    if request.method == 'POST':
        comment.delete()
        return redirect('post', pk=comment.post.id)
    return render(request, 'main/delete.html', {'obj': comment})

@login_required(login_url='/login')
def createBook(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.save()
            messages.success(request, 'Your book will be validated by the admin soon')
            return redirect('home')
    context = {'form': form}
    return render(request, 'main/post_form.html', context)

@login_required(login_url='/login')
def editProfile(request):
    profile = request.user. profile
    profile_form = ProfileForm(instance= profile)
    user_form = UserForm(instance= request.user)

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance= profile)
        user_form = UserForm(request.POST, request.FILES, instance= request.user)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile', pk=profile.id)

    context = {'profile_form': profile_form, 'user_form': user_form}
    return render(request, 'main/edit_profile.html', context)


def bookClubList(request):
    clubs= BookClub.objects.all()
    context= {'clubs': clubs}
    return render(request, 'main/BookClub_list.html', context)

def bookClubDetail(request, pk):
    club = get_object_or_404((BookClub), id=pk)
    is_member = request.user.is_authenticated and club.members.filter(id= request.user.profile.id).exists()
    is_host = request.user.is_authenticated and club.host == request.user.profile

    if request.method == 'POST':
        if not request.useer.is_authenticated:
            user_profile = request.user.profile
            return redirect('login')
        action = request.POST.get('action')
        if action =='join':
            club.members.add(request.user.profile)
        elif action =='leave':
            club.members.remove(request.user.profile)
        return redirect('bookClub-detail', pk=club.id)

    context = {'club': club, 'is_member': is_member, 'is_host': is_host}
    return render(request, 'main/BookClub_detail.html', context)


@login_required(login_url='/login')
def createBookClub(request):
    form = BookClubForm()
    if request.method == 'POST':
        form = BookClubForm(request.POST, request.FILES)
        if form.is_valid():
            club = form.save(commit=False)
            club.host = request.user.profile
            club.save()
            club.members.add(request.user.profile)
            return redirect('bookClub-detail', pk=club.id)
    context = {'form': form}
    return render(request, 'main/post_form.html', context)


@login_required(login_url='/login')
def deleteBookClub(request, pk):
    club = get_object_or_404((BookClub), pk=pk)

    if request.user.profile != club.host:
        return redirect('bookClub-detail', pk=club.id)

    if request.method == 'POST':
        club.delete()
        return redirect('bookClub-list')
    return render(request, 'main/delete.html', {'obj': club})










