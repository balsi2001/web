from django.shortcuts import render
from django.http import *
from .forms import CommentModelForm
from .models import Comment
def index(request):
    return render(
        request,
        "comments/index.html",
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
   

def singel_comment(request):
    comment_list=Comment.objects.all()
    context={
        'comment_list':comment_list
    }
    return render(
        request,
        "comments/signle_comment.html",
        context
    )

def write_comment(request):
    
    if request.method == "POST":
        form = CommentModelForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse("儲存成功")

    form = CommentModelForm()

    context = {
        "form": form
    }

    return render(
        request,
        "comments/write_comment.html", context,
    )
