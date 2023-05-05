from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("create/", views.create, name="create-thread"),
    path("detail/", views.detail, name="detail-thread"),
    path("profil/", views.profil, name="profil"),
    path("changepassword/", views.changepassword, name="changepassword"),
]
