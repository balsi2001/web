from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("all_comments/", views.all_comments),
    path("write/", views.write_comment),
    path("comment/<int:pk>", views.CommentDetailView.as_view(), name="Comment_detail"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login")
]