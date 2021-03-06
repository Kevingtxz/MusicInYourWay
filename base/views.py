from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

def registerPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            StandardUser.objects.create(user=user)
            messages.success(request, "Account was created for " + username)
            return redirect("login")

    context = {"form": form}
    return render(request, "accounts/register.html", context)

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("questions")
        else:
            messages.info(request, "Username OR password is incorrect")
    context = {}
    return render(request, "base/login.html", context)


def logoutUser(request):
    logout(request)
    return redirect("base")


# @login_required(login_url="login")
def homePage(request):
    context = {}
    return render(request, "base/home.html", context)

# @login_required(login_url="login")
def musicsPage(request):
    musics = Music.objects.all()
    context = {
        "musics" : musics,
    }
    return render(request, "base/musics.html", context)