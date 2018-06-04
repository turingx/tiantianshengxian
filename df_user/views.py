#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
import hashlib
from df_user.models import UserInfo

# Create your views here.

def register(request):
    return render(request, "user_template/register.html")

def register_handle(request):
    uname = request.POST['user_name']
    upwd = request.POST['pwd']
    ucpwd = request.POST['cpwd']
    uemail = request.POST['email']
    uallow = request.POST['allow']

    if upwd != ucpwd:
        return HttpResponse("两次输入的密码不一致")

    #使用sha1加密密码
    encry = hashlib.sha1()
    encry.update(upwd)
    encry_pwd = encry.hexdigest()

    userInfo = UserInfo()
    userInfo.uname = uname
    userInfo.upwd = encry_pwd
    userInfo.uemail = uemail
    userInfo.save()


    return HttpResponse("注册成功")


def login(request):
    return render(request, "user_template/login.html")
