from django.urls import path
from .import views
urlpatterns = [
    path('',views.home, name='home'),
    path('experience/', views.experience, name='experience'),
    path('projects/', views.projects, name='projects'),
    path('skills/', views.skills, name='skills'),
    path('Education/', views.Education, name='Education'),
]