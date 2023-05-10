from django.urls import path
from django.urls import re_path as url
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.loginUser, name="login"),
    path("profile/", views.profile, name="profile"),
    path("changepassword/", views.changepassword, name="changepassword"),
    path("create/", views.create, name="create-thread"),
    path("coupons/<int:coupon_id>/", views.detail, name="detail-thread"),
    path('logout/', views.logoutUser, name="logout"),
    url(r'^upvote/(?P<id>\d+)/$', views.upvote, name='upvote'),
    url(r'^downvote/(?P<id>\d+)/$', views.downvote, name='downvote'),
]
 