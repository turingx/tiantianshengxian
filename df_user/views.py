from django.shortcuts import render

# Create your views here.


def register(request):
    return render(request, "user_template/register.html")


def login(request):
    return render(request, "user_template/login.html")
