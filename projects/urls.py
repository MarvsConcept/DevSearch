from django.urls import 
from .import views

urlpatterns = [
    path('', views.projects, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),
    path('create-project', views.CreateProject, name='create-project'),
    path('update-project/<str:pk>/', views.UpdateProject, name='update-project'),
    path('delete-project/<str:pk>/', views.DeleteProject, name='delete-project')
]
