from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import get_object_or_404, redirect, render

from .forms import createCouponForm, createUserForm, getUserForm
from .models import Coupon


# Form for the signup of a new user
def signup(request):
    if request.user.is_authenticated:
        return redirect("home")
        # return redirect("loggedin")
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


# Form for the login of a user
def loginUser(request):
    form = getUserForm()
    if request.user.is_authenticated:
        return redirect("home")
        # return redirect("loggedin")
    else:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, password=password, username=username)

            if user is not None:
                login(request, user)
                return redirect("home")
                # return redirect("loggedin")
            else:
                messages.info(request, "Username or Password is incorrect")

    return render(request, "login.html", {"form": form})


# Form for the profile of the logged in user
@login_required(login_url="login")
def profile(request):
    if request.method == "GET":
        return render(request, 'profile.html')



# Form for the home view
def home(request):
    coupons = Coupon.objects.all()
    return render(request, "home.html", {"coupons": coupons})



from django.contrib.auth.decorators import login_required


@login_required
def create(request):
    if request.method == "POST":
        form = createCouponForm(request.POST)
        if form.is_valid():
            coupon = form.save(commit=False)
            coupon.user = request.user
            coupon.save()
            return redirect("detail-thread", coupon_id=coupon.pk)
    else:
        form = createCouponForm()
    return render(request, "threadcreate.html", {"form": form})
# Form for the detail view of a thread
def detail(request, coupon_id):
    coupon = get_object_or_404(Coupon, pk=coupon_id)
    return render(request, "threaddetail.html", {"coupon": coupon})


# Form to change password
def changepassword(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user.request.POST)
        if form.is_valid:
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password changed successfully")
            return redirect("profile")
    else:
        form = PasswordChangeForm(request.user.request.POST)
    return render(request, "changepassword.html", {"form": form})


# Form to logout user
def logoutUser(request):
    logout(request)
    return redirect("home")


def upvote(request,id):
    coupon = get_object_or_404(Coupon, pk=id)
    if request.method == "POST":
        coupon.score += 1
        coupon.save()
    return redirect("home")

def downvote(request,id):
    coupon = get_object_or_404(Coupon, pk=id)
    if request.method == "POST":
        coupon.score -= 1
        coupon.save()
    return redirect("home")

def logoutUser(request):
    logout(request)
    return redirect('home')
        