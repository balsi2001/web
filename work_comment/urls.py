from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("all_comments/", views.all_comments),
    path("write/", views.write_comment),
    path("single_comments/",views.singel_comment)
    # path("comment/<int:id>"),
]