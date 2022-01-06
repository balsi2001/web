from django.shortcuts import render
from django.http import *

def index(request):
    return render(
        request,
        "comments/index.html",
    )
