from django.forms import ModelForm
from .models import Post, Book


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