from django.urls import path
from . import views

urlpatterns  = [
    path("", views.index, name="index"),
#    path("<str:name>", views.index, name="index"),  # form test
    path("home/", views.home, name="home"),
    path("index/", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("projects/", views.projects, name="projectmenu"),
    path("projectmenu/", views.projectmenu, name="projectmenu"),
    path("resume/", views.resume, name="resume"),
    path("test/", views.test, name="test"),   
    path("fars/", views.fars, name="fars"),
    path("fethealth/", views.fethealth, name="fethealth"),   
    path("dtsc691menu/", views.dtsc691menu, name="dtsc691menu"),
    path("dtsc691/dtsc691_jupnotebook/", views.dtsc691_jupyter_notebook, name="dtsc691_jupynotebook"),
    path("dtsc691/state_heatmap/", views.state_heatmap, name="state_heatmap"),
    path("dtsc691/us_cities_map/", views.us_cities_map, name="us_cities_map"),
    path("dtsc691/world_cities_map/", views.world_cities_map, name="world_cities_map"),
    path("dtsc691/project_analyses/", views.project_analyses, name="project_analyses"),
    path("dtsc691/csv/", views.csv, name="csv"),
    path("dtsc691/json/", views.json, name="json"),

]