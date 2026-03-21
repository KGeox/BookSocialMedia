from django.db import models
from django.contrib.auth.models import  User



# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image =models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(blank=True,null=True)
    streak = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Book(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    genre = models.TextField()
    image = models.ImageField(upload_to='posts')
    summary = models.TextField(max_length=500, null=True, blank=True)



    def __str__(self):
        return self.title

class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    Book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reference = models.TextField(max_length=100)
    content = models.TextField(max_length = 500)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='posts', null=True, blank=True)
    reads = models.IntegerField(default=0)
    # similar = models.ManyToManyField(Post, blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
