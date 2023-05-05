from django.shortcuts import render, redirect
from .forms import getUserForm, createUserForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm

coupons = [
    {
        "ID": "1",
        "expire_date": "2021-10-01",
        "discount_amount": "10%",
        "name": "Gutschein 1",
        "score": "5",
        "comments": "Kommentar1",
        "hashtag": "#Gutschein1",
    },
    {
        "ID": "2",
        "expire_date": "2021-10-01",
        "discount_amount": "10%",
        "name": "Gutschein 2",
        "score": "5",
        "comments": "Kommentar1",
        "hashtag": "#Gutschein1",
    },
    {
        "ID": "3",
        "expire_date": "2021-10-01",
        "discount_amount": "10%",
        "name": "Gutschein3",
        "score": "5",
        "comments": "Kommentar1",
        "hashtag": "#Gutschein1",
    },
    {
        "ID": "4",
        "expire_date": "2021-10-01",
        "discount_amount": "10%",
        "name": "Gutschein 4",
        "score": "5",
        "comments": "Kommentar1",
        "hashtag": "#Gutschein1",
    },
    {
        "ID": "5",
        "expire_date": "2021-10-01",
        "discount_amount": "10%",
        "name": "Gutschein 5",
        "score": "5",
        "comments": "Kommentar1",
        "hashtag": "#Gutschein1",
    },
    {
        "ID": "6",
        "expire_date": "2021-10-01",
        "discount_amount": "10%",
        "name": "Gutschein 6",
        "score": "5",
        "comments": "Kommentar1",
        "hashtag": "#Gutschein1",
    },
]

# Form for the login of a user
def login(request):
    form = getUserForm()
    if request.user.is_authenticated:
        return redirect("loggedin")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, password=password, username=username)

            if user is not None:
                login(request, user)
                return redirect("loggedin")
            else:
                messages.info(request, "Username or Password is incorrect")

    return render(request, "login.html", {"form": form})

# Form for the home view
def home(request):
    context = {"coupons": coupons}
    return render(request, "home.html", context)

# Form for the profil of the logged in user
# @login_required(login_url="login")
def profil(request):
    return render(request, "profil.html")

# Form for the signup of a new user
def signup(request):
    if request.user.is_authenticated:
        return redirect("loggedin")
    else:
        form = createUserForm()
        if request.method == "POST":
            form = createUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(request, "Account created for " + user)
                return redirect("login")

    return render(request, "signup.html", {"form": form})

# Form for the creation of a thread
def create(request):
    return render(request, "threadcreate.html")

# Form for the detail view of a thread
def detail(request):
    return render(request, "threaddetail.html")

# Form to change password
def changepassword(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user.request.POST)
        if form.is_valid:
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password changed successfully")
            return redirect("profil")
    else:
        form = PasswordChangeForm(request.user.request.POST)
    return render(request, "changepassword.html", {"form": form})

# Form to logout user
def logoutUser(request):
    logout(request)
    return redirect("home")
