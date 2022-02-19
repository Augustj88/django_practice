from django.shortcuts import render, redirect
from django.contrib.auth.models import User #모델불러오기 장고내장user
from .models import Article, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    articles = Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


@login_required(login_url='signin')
def new(request):
    if request.method == 'POST':
        article = Article.objects.create(
            author = request.user,
            title = request.POST['title'],
            content = request.POST['content']
        )
        return redirect('detail', article.pk)
        #글을 작성하고 글이 보이는 페이지로 이동, 글의 세부페이지로 이동 - article.pk pk는 db의 id값이다.
    else:
        return render(request, 'blog/new.html')

@login_required(login_url='signin')
def detail(request, pk): #사용자가 어떤 글을 보고자 했는지 받아야한다. 그래서 pk사용한다.
    article = Article.objects.get(pk=pk)
    # 댓글을 위한 부분
    if request.method == 'POST': # create 를 위한 부분
        comment = Comment.objects.create(
            author=request.user,
            article=article,
            comment=request.POST['comment'],
        )
        return redirect('detail', article.pk) #왼쪽 pk는 고유한 필드명, 오른쪽 pk는 변수명(변경가능)
    else: # read 를 위한 부분
        comments = Comment.objects.filter(article=article)
        return render(request, 'blog/detail.html', {'article': article, 'comments': comments})
        # 왼쪽 article은 html에서 쓰는 변수명, 오른쪽 article은 views의 변수명

@login_required(login_url='signin') # 로그인하지 않을 경우 리다이렉트
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    # 남이 쓴 글에 대해서 수정 요청을 방지
    if request.user == article.author:
        if request.method == 'POST':
            # POST 일때는 글 수정
            article.title = request.POST['title']
            article.content = request.POST['content']
            article.save()
            return redirect('detail', article.pk)
        else:
            return render(request, 'blog/edit.html', {'article': article})
    else:
        return render(request, 'blog/edit.html', {'error': '잘못된 접근입니다.'})

@login_required(login_url='signin') # 로그인하지 않을 경우 리다이렉트
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    # 남이 쓴 글에 대해서 수정 요청을 방지
    if request.user == article.author:
        article.delete()
        return redirect('index')
    else:
        return redirect('detail', article.pk)

@login_required(login_url='signin') # 로그인하지 않을 경우 리다이렉트
def delete_comment(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    # 남이 쓴 글에 대해서 수정 요청을 방지
    if request.user == comment.author:
        comment.delete()
        return redirect('detail', article_pk)
    #else문은 삭제해도 무방함
    else:
        return redirect('detail', article_pk)