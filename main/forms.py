from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Post, Book, Profile, BookClub


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'Book', 'content', 'reference', 'image']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['Book'].queryset = Book.objects.filter(valid=True)

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['author', 'title', 'genre', 'image', 'summary']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image', 'bio']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

class BookClubForm(ModelForm):
    class Meta:
        model = BookClub
        fields = ['name', 'description', 'current_book']