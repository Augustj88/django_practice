# all code is added from class

from django.urls import path
from . import views


urlpatterns = [
    path('signup', views.signup, name='signup'), #signup으로 들어오면 views.signup을 실행한다.
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout')
]