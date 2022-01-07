from django import forms
from django.db import models
from .models import Comment
from django.core.exceptions import ValidationError

class CommentModelForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = "__all__"

        labels = {
            "comment_title": "標題",
            "comment_name": "作者",
            "comment_company": "公司名稱",
            "comment_score": "評分",
            "comment_context": "評論內容"
        }
