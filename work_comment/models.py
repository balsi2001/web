from django.db import models

# Create your models here.
class Comment(models.Model):
    comment_title = models.CharField(max_length=15)
    comment_name = models.CharField(max_length=10, null=True)
    comment_company = models.CharField(max_length=15)
    comment_score = models.IntegerField()    
    comment_context = models.CharField(max_length=256)

    def __str__(self):
        return self.comment_title
