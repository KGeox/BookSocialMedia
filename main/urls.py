from django.urls import path
from . import views

urlpatterns = [


    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('profile', views.profile, name='profile'),

    path('register', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('login/', views.loginPage, name='login'),
    path('post/<str:pk>', views.post, name="post"),
    path('create-post/', views.createPost, name='create-post'),
    path('update-post/<str:pk>/', views.updatePost, name='update-post'),
    path('delete-post/<str:pk>/', views.deletePost, name="delete-post"),

]