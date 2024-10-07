from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    path("index2/", views.index, name="index"),
    path("", views.articles_list, name="articles_list"),
    path("<int:id>/", views.article_detail, name="article_detail"),
]