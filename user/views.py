from django.shortcuts import render, redirect  #redirect추가
from django.contrib import auth #로그인 관련함수
from django.contrib.auth.models import User #로그인 관련함수
from django.contrib.auth.decorators import login_required #로그인 관련함수

# Create your views here.
def signup(request):
    if request.method == 'POST':
        # 아이디가 중복이라면
        found_user = User.objects.filter(username = request.POST['username'])
        if len(found_user) > 0:
            return render(request, 'user/signup.html'), {'error':'username이 이미 존재합니다.'}
        else:
            new_user = User.objects.create_user(  #User는 django의 기본 모델
                username = request.POST['username'], #signup.html의 'username'
                password = request.POST['password'] #signup.html의 'password'
        )
            auth.login(request, new_user)
            return redirect('index') #로그인 후에는 index페이지로 이동
            # method가 post 형식으로 정보를 보낼 때 - 회원가입 + 로그인
    else:
        # 그냥 링크타고 들어왔을 때
        # 회원가입 정보 입력 페이지 보여준다.
        return render(request, 'user/signup.html')

def signin(request):
    if request.method == 'POST':
        found_user = auth.authenticate(request,
           username = request.POST['username'],
           password = request.POST['password']
        )
        if found_user is not None:
            auth.login(request, found_user)
            return redirect('index')
        else:
            return render(request, 'user/signin.html', {'error':'유저가 이미 존재합니다.'})
    else:
        return render(request, 'user/signin.html')

@login_required(login_url='signin') # 로그인 안했으면 signin 페이지로 간다.
# 로그인이 되었다면 아래 함수 실행
def signout(request):
    auth.logout(request)
    return redirect('index') #index함수로 바뀐다.