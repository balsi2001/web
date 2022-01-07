from django import forms
from django.db import models
from .models import Comment
from django.core.exceptions import ValidationError

class CommentModelForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = "__all__"

        widgets = {
            "comment_title": forms.TextInput(attrs={"class": "form-control", "placeholder": "為這篇評論想個有趣的標題", "style": "margin-bottom: 2%;"}),
            "comment_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "填入姓名", "style": "margin-bottom: 2%;"}),
            "comment_company": forms.TextInput(attrs={"class": "form-control", "placeholder": "填入公司名稱", "style": "margin-bottom: 2%;"}),
            "comment_score": forms.RadioSelect(attrs={"class": "form-control", "style": "margin-bottom: 2%;"}),
            "comment_context": forms.Textarea(attrs={"class": "form-control", "rows": "4", "style": "margin-bottom: 2%;"})
        }

        labels = {
            "comment_title": "標題",
            "comment_name": "作者",
            "comment_company": "公司名稱",
            "comment_score": "評分",
            "comment_context": "評論內容"
        }
