from django.urls import path 
from . import views


urlpatterns = [
    path('home/', views.home, name = 'Home Section'),
    path('project/<str:project_id>/', views.project_detail, name='Project Detail'),
]