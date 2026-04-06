from django.contrib import admin
from .models import Post, Book, Profile, Comment, BookClub
# Register your models here.

admin.site.register(Post)

admin.site.register(Book)

admin.site.register(Profile)

admin.site.register(Comment)

admin.site.register(BookClub)