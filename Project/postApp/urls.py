from django.urls import path
from . import views


urlpatterns = [
    path("register", views.register),
    path("login", views.login),
    path("post", views.posts.as_view()),
    path("post/<int:pk>/", views.postsDetails.as_view()),
    path("authors/<int:pk>/", views.authorDetails.as_view()),

]
