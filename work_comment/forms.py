from django import forms
from .models import Comment

class CommentModelForm(forms.ModelForm):
    CHOICES = [
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5")
    ]

    comment_title = forms.CharField(
        widget = forms.TextInput(attrs={"class": "form-control", "placeholder": "為這篇評論想個有趣的標題", "style": "margin-bottom: 2%;"}),
        label = "標題",
        required = True
    )

    comment_name = forms.CharField(
        widget = forms.TextInput(attrs={"class": "form-control", "placeholder": "填入姓名", "style": "margin-bottom: 2%;"}),
        label = "作者",
        required = True
    )

    comment_company = forms.CharField(
        widget = forms.TextInput(attrs={"class": "form-control", "placeholder": "填入公司名稱", "style": "margin-bottom: 2%;"}),
        label = "公司名稱",
        required = True
    )

    comment_score = forms.ChoiceField(
        choices = CHOICES,
        widget = forms.RadioSelect(),
        label = "評分",
        required = True
    )

    comment_context = forms.CharField(
        widget = forms.Textarea(attrs={"class": "form-control", "rows": "4", "style": "margin-bottom: 2%;"}),
        label = "評論內容",
        required = True
    )
    
    class Meta:
        model = Comment
        fields = "__all__"
