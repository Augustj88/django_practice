from django.db import models
from django.contrib.auth.models import User #django내장 user모델

# Create your models here.
class Article(models.Model):
    class Meta:
        db_table = "article"

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #없는 유저면 안 되므로 foreign key / user입장에서 one to many / 유저가 삭제되는경우 연결데이터도 함께 삭제(foreignkey에서는)
    title = models.CharField(max_length=256)
    content = models.TextField() #길어져도 상관없을때 textfield
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    class Meta:
        db_table = "comment"

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #댓글작성자
    comment = models.CharField(max_length=256) #짧게 받을 때 한줄형태, char필드는 꼭 길이 명시할 것!
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)