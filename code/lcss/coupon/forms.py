from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Coupon, Comment


# Form to create a new User
class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        ]


# Form to login a User
class getUserForm(forms.ModelForm):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        model = User
        widgets = {
            "password": forms.PasswordInput(),
        }
        fields = [
            "username",
            "password",
        ]


class createCouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        widgets = {
            "expiring_date": forms.DateInput(attrs={"type": "date"}),
        }
        fields = [
            "name",
            "expiring_date",
            "discount_amt",
        ]


class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))

    class Meta:
        model = Comment
        fields = ("text",)
