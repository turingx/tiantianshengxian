#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
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

    print(uemail)
    if upwd != ucpwd:
        return HttpResponse("两次输入的密码不一致")
    '''
    if uname == None:
        context = {'temp':"用户名为空"}
        return render(request, "user_template/register.html", context)
    if upwd == None:
        context = {'temp': "密码为空"}
        return render(request, "user_template/register.html",  context)
    if uemail == None:
        context = {'temp': "邮箱为空为空"}
        return render(request, "user_template/register.html",  context)
'''

    #使用sha1加密密码
    encry = hashlib.sha1()
    encry.update(upwd)
    encry_pwd = encry.hexdigest()

    userInfo = UserInfo()
    userInfo.uname = uname
    userInfo.upwd = encry_pwd
    userInfo.uemail = uemail
    userInfo.save()
    return redirect('/user/login')
    #return HttpResponse("注册成功")

def register_exist(request):
    username = request.GET['user_name']
    print(username)
    count = UserInfo.objects.filter(uname=username).count()
    return JsonRespones({'count':count})



def login(request):
    return render(request, "user_template/login.html")


def login_handle(request):
    uname = request.POST['username']
    upwd = request.POST['pwd']

    #使用sha1加密密码
    encry = hashlib.sha1()
    encry.update(upwd)
    encry_pwd = encry.hexdigest()

    sel_uname_num = UserInfo.objects.filter(uname=uname).count()
    if sel_uname_num != 0:
        sel_pwd = UserInfo.objects.filter(uname=uname)[0].upwd
        if sel_pwd == encry_pwd:
            request.session['sess_uname'] = uname
            return redirect("/user/user_center")

        else:
            return HttpResponse("用户名或密码错误")
    else:
        return HttpResponse("用户名或密码错误")

def user_center(request):
    name = request.session['sess_uname']
    print(name)
    user_email =  UserInfo.objects.filter(uname=name)[0].uemail
    user_address =  UserInfo.objects.filter(uname=name)[0].uaddress
    context = {'name': name, 'uemail':user_email, 'uaddress':user_address}
    return render(request, "user_template/user_center_info.html", context)

def order(request):
    return render(request, "user_template/user_center_order.html")

def site(request):
    return render(request, "user_template/user_center_site.html")
   # return HttpResponse('a')




