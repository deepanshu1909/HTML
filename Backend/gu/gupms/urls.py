from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views  

urlpatterns = [
   path('', views.home, name="home"),
   path('signup', views.signup, name="signup"),
   path('signin', views.signin, name="signin"),
   path('signout', views.signout, name="signout"),
   path('mainpage', views.mainpage, name="mainpage"),
   path('select', views.select, name="select"),
   path('first_year', views.first_year, name="first_year"),
   path('second_year', views.second_year, name="second_year"),
   path('third_year', views.third_year, name="third_year"),
   path('fourth_year', views.fourth_year, name="fourth_year"),
   path('send/', views.send, name="send"),
   path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
   path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
   path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
   path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
