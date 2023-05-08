from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.loginUser, name="login"),
    path("profile/", views.profile, name="profile"),
    path("changepassword/", views.changepassword, name="changepassword"),
    path("create/", views.create, name="create-thread"),
    path("coupons/<int:coupon_id>/", views.detail, name="detail-thread"),
]
