from django.urls import path
from . import views

urlpatterns = [


    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('profile/edit/', views.editProfile, name='edit_profile'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('register', views.registerPage, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('login/', views.loginPage, name='login'),
    path('post/<str:pk>', views.post, name="post"),
    path('book/<str:pk>', views.book, name="book"),
    path('create-book', views.createBook, name="create-book"),
    path('create-post/', views.createPost, name='create-post'),
    path('update-post/<str:pk>/', views.updatePost, name='update-post'),
    path('delete-post/<str:pk>/', views.deletePost, name="delete-post"),
    path('delete-comment/<str:pk>/', views.deleteComment, name="delete-comment"),
    path('clubs/', views.bookClubList, name='bookClub-list'),
    path('clubs/create/', views.createBookClub, name='create-bookClub'),
    path('clubs/<str:pk>/', views.bookClubDetail, name='bookClub-detail'),
    path('clubs/<str:pk>/delete/', views.deleteBookClub, name='delete-bookclub'),
]