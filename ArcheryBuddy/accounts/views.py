from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, RegisterForm

# Create your views here.
def login_view(request):
    ctx = {}
    ctx["errors"] = []

    if request.method == "POST":
        pseudo = request.POST["pseudo"]
        password = request.POST["password"]
        user = authenticate(request, pseudo=pseudo, password=password)
        if user is not None:
            login(request, user)
            ctx["errors"] = []
            return render(request, "accounts/login_done.html", context=ctx)
        ctx["errors"].append("identifiants erronés")
        return render(request, "accounts/login.html", context=ctx)

    elif request.method == "GET":
        form = LoginForm()
        ctx["form"] = form
        return render(request, "accounts/login.html", context=ctx)

    else:
        ctx["errors"].append(f'méthode "{request.method}" interdite')
        return render(request, "accounts/login.html", context=ctx)


def register_view(request):
    form = RegisterForm()
    ctx = {"form": form}
    return render(request, "accounts/register.html", context=ctx)


@login_required()
def logout_view(request):
    logout(request)
    return redirect("login")


@login_required()
def profile_view(request):
    pass
