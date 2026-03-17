from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('profile', views.profile, name='profile'),

    path('post/<str:pk>', views.post, name="post"),
    path('create-post/', views.createPost, name='create-post'),
    path('update-post/<str:pk>', views.updatePost, name='update-post'),

]