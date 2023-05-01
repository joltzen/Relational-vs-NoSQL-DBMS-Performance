from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Form to create a new User
class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields =["username", "first_name", "last_name", "email", "password1", "password2"]
        
# Form to login a User
class getUserForm(forms.ModelForm):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        model = User
        widgets = {
            "password": forms.PasswordInput(),
        }
        fields = ["username", "password"]
