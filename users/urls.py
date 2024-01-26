from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    
    path('', views.profiles, name="profiles"),
    path('profile/<str:pk>/', views.UserProfile, name='user-profile'),
    path('account/', views.userAccount, name='account'),
    path('edit-account/', views.editAccount, name='edit-account'),
    path('create-skill/', views.CreateSkill, name='create-skill'),
    path('update-skill/<str:pk>/', views.UpdateSkill, name='update-skill'),
    path('delete-skill/<str:pk>/', views.DeleteSkill, name='delete-skill'),
    
    path('inbox/', views.inbox, name='inbox'),
]

