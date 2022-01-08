from django.db import models
from django.urls import reverse

# Create your models here.
class Comment(models.Model):
    comment_title = models.CharField(max_length=15)
    comment_name = models.CharField(max_length=10, null=True)
    comment_company = models.CharField(max_length=15)
    comment_score = models.IntegerField()
    comment_context = models.CharField(max_length=256)

    def get_url(self):
        return reverse("Comment_detail", args=[str(self.id)])

    class Mata:
        ordering = ['-comment_title']
    def __str__(self):
        return self.comment_title
