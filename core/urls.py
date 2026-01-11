from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("thematic-areas/", views.thematic_areas, name="thematic_areas"),
    path("programs/", views.programs, name="programs"),
    path("leadership/", views.leadership, name="leadership"),
    path("projects/", views.projects_list, name="projects"),
    path("projects/<slug:slug>/", views.project_detail, name="project_detail"),
    path("news/", views.news_list, name="news"),
    path("news/<slug:slug>/", views.news_detail, name="news_detail"),
    path("contact/", views.contact, name="contact"),
]
