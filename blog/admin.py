from django.contrib import admin
from .models import Article, Comment

# Register your models here.
# 데이터 수정할 때 용이함, django ninja의 경우에 사용하지 않음
admin.site.register(Article)
admin.site.register(Comment)
