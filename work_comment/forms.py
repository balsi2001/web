from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Comment
from django.contrib.auth.models import User

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

class SignupForm(UserCreationForm):
    username = forms.CharField(
        label = "帳號",
        widget = forms.TextInput(attrs={"class": "form-control"})
    )

    password1 = forms.CharField(
        label = "密碼",
        widget = forms.PasswordInput(attrs={"class": "form-control"})
    )

    password2 = forms.CharField(
        label = "密碼確認",
        widget = forms.PasswordInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

class LoginForm(forms.ModelForm):
    username = forms.CharField(
        label = "帳號",
        widget = forms.TextInput(attrs={"class": "form-control"})
    )

    password = forms.CharField(
        label = "密碼",
        widget = forms.PasswordInput(attrs={"class": "form-control"})
    )

    class Meta:
        model = User
        fields = ("username", "password")
