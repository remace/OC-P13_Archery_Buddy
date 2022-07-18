from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from accounts.models import User
from accounts.forms import LoginForm, RegisterForm

# Create your views here.
def login_view(request):
    ctx = {}
    ctx["errors"] = []
    form = LoginForm()
    ctx["form"] = form

    if request.method == "POST":
        pseudo = request.POST["pseudo"]
        password = request.POST["password"]
        user = authenticate(request, pseudo=pseudo, password=password)
        print(user)
        if user is not None:
            login(request, user)
            ctx["errors"] = []
            return render(request, "accounts/login.html", context=ctx)
        else:
            ctx["errors"].append("identifiants erronés")
            return render(request, "accounts/login.html", context=ctx)

    elif request.method == "GET":
        return render(request, "accounts/login.html", context=ctx)

    else:
        ctx["errors"].append(f'méthode "{request.method}" interdite')
        return render(request, "accounts/login.html", context=ctx)


def register_view(request):
    ctx = {}
    ctx["errors"] = []
    form = RegisterForm()
    ctx["form"] = form

    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        pseudo = request.POST.get("pseudo")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if password != password2:
            redirect("register")

        user = User.objects.create(
            pseudo=pseudo,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save()
        return redirect("login")

    elif request.method == "GET":
        return render(request, "accounts/register.html", context=ctx)

    else:
        ctx["errors"].append(f'méthode "{request.method}" interdite')
        return render(request, "accounts/register.html", context=ctx)


@login_required(login_url="/user/login/")
def logout_view(request):
    logout(request)
    return redirect("login")
