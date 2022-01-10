from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.http import *
from .forms import CommentModelForm
from .models import Comment
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
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
class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/login.html"
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
@login_required
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

    def get(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        
        prev = Comment.objects.filter(id__lt=comment.id).last()
        next = Comment.objects.filter(id__gt=comment.id).first()

        context = {
            "comment": comment,
            "previous": prev,
            "next": next
        }

        return render(request, self.template_name, context)
