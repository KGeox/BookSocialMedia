from django.contrib import admin
from .models import Post, Book, Profile, Comment
# Register your models here.

admin.site.register(Post)

admin.site.register(Book)

admin.site.register(Profile)

admin.site.register(Comment)
