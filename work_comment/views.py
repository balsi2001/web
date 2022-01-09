from django.views import generic
from django.shortcuts import render
from django.http import *
from .forms import CommentModelForm
from .models import Comment
from django.contrib import messages

def index(request):
    length = Comment.objects.all().count()
    comment_list = Comment.objects.all()[length-3::-1]
    print(comment_list)
    context = {
        "comment_list": comment_list
    }

    return render(
        request,
        "comments/index.html",
        context
    )

def all_comments(request):
    comment_list=Comment.objects.all()
    context={
        'comment_list':comment_list
    }

    return render(
        request,
        "comments/all_comments.html",
        context
    )

def write_comment(request):
    
    if request.method == "POST":
        form = CommentModelForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "儲存成功")

    form = CommentModelForm()

    context = {
        "form": form
    }

    return render(
        request,
        "comments/write_comment.html", context,
    )

class CommentDetailView(generic.DetailView):
    model = Comment
    template_name = "comments/single_comment.html"
