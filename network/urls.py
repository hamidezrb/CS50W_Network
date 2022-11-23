
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_post", views.new_post, name="new_post"),
    path("following", views.following, name="following"),
    path("edit_post", views.edit_post, name="edit_post"),
    path("profile/<int:user_id>", views.profile, name="profile"),
    path("like_post/<int:post_id>", views.like_post, name="like_post"),
    path("follow_user", views.follow_user, name="follow_user")
    
]
